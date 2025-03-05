from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

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
        assert self.gainers_df.symbol.dtype == 'O', \
                f'Expected string column symbol: {self.gainers_df.symbol.dtype}'
        assert self.gainers_df.symbol.str.isupper().all(), 'Wrong formatting for symbol: not all uppercase'
        lengths = pd.Series([len(x) for x in self.gainers_df.symbol]) 
        assert (lengths < 6).all(), 'Wrong formatting for symbol: some len > 5' + str(self.gainers_df.symbol)
        assert self.gainers_df.price.dtype == 'float', \
                f'Expected numeric column price: {self.gainers_df.price.dtype}'
        assert self.gainers_df.price_change.dtype == 'float', \
                f'Expected numeric column price_change: {self.gainers_df.price_change.dtype}'
        assert self.gainers_df.price_percent_change.dtype == 'float', \
                f'Expected numeric column price_percent_change: {self.gainers_df.price_percent_change.dtype}'
        old_price = self.gainers_df.price - self.gainers_df.price_change
        percent_change_calculated = (self.gainers_df.price - old_price) / old_price * 100
        assert (self.gainers_df.price_percent_change - percent_change_calculated < 1).all(), \
                'Columns do not add up' + str(test_df)

    def normalize(self):
        gainers_df = pd.read_html(self.name + '.html', flavor = 'lxml', displayed_only = False)[0]
        gainers_df = gainers_df.loc[:, self.headers]
        gainers_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        self.gainers_df = gainers_df

    def save_with_timestamp(self):
        stamped_filename = self.name + datetime.now().strftime('%Y%m%d-%H%M%S') + '.csv'
        self.gainers_df.to_csv(stamped_filename, index = False)
