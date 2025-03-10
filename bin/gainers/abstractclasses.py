from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd
from logger import write_log

class GainerDownload(ABC):
    headers = {'user-agent' : 'rn7ena@virginia.edu'}

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def download(self):
        pass

class GainerProcess(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def check(self):
        # dataframe has correct shape
        assert isinstance(self.gainers_df, pd.DataFrame)
        assert self.gainers_df.shape[1] == 4
        # symbol format
        assert self.gainers_df.symbol.dtype == 'O', \
                f'Expected string column symbol: {self.gainers_df.symbol.dtype}'
        assert self.gainers_df.symbol.str.isupper().all(), 'Wrong formatting for symbol: not all uppercase'
        lengths = pd.Series([len(x) for x in str(self.gainers_df.symbol)]) 
        assert (lengths < 7).all(), 'Wrong formatting for symbol: some len > 6' + str(self.gainers_df.symbol.loc[lengths > 6])
        # number formatting
        assert self.gainers_df.price.dtype == 'float', \
                f'Expected numeric column price: {self.gainers_df.price.dtype}'
        assert self.gainers_df.price_change.dtype == 'float', \
                f'Expected numeric column price_change: {self.gainers_df.price_change.dtype}'
        assert self.gainers_df.price_percent_change.dtype == 'float', \
                f'Expected numeric column price_percent_change: {self.gainers_df.price_percent_change.dtype}'
        # numbers should add up
        old_price = self.gainers_df.price - self.gainers_df.price_change
        percent_change_calculated = (self.gainers_df.price - old_price) / old_price * 100
        assert (self.gainers_df.price_percent_change - percent_change_calculated < 1).all(), \
                'Columns do not add up' + str(test_df)

    def normalize(self):
        write_log(self.choice, f'Reading {self.name}.html')
        gainers_df = pd.read_html(self.name + '.html', flavor = 'lxml', displayed_only = False)[0]
        gainers_df = gainers_df.loc[:, self.headers]
        gainers_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        self.gainers_df = gainers_df

    def save_with_timestamp(self):
        stamped_filename = self.name + self.timestamp + '.csv'
        try:
            self.gainers_df.to_csv(stamped_filename, index = False)
            write_log(self.choice, f'Successfully saved {stamped_filename}')
        except Exception as e:
            write_log(self.choice, f'Error saving {stamped_filename}: {e}')
