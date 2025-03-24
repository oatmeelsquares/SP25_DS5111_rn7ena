import requests
import pandas as pd
from abstractclasses import GainerDownload, GainerProcess
from logger import write_log

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        self.choice = 'yahoo'
        self.url = 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'
        write_log('yahoo', f'Initializing yahoo downloader with url {self.url}')

    def download(self):
        write_log('yahoo', f'Retreiving html from {self.url}')
        response = requests.get(self.url, headers = self.headers)
        if response.status_code == 200:
            with open('ygainers.html', 'w') as ygainers_file:
                ygainers_file.write(response.text)
            write_log('yahoo', f'Response successful: status code {response.status_code}')
        else:
            write_log('yahoo', f'Error in yahoo request: {response.status_code}')

class GainerProcessYahoo(GainerProcess):
    def __init__(self, timestamp):
        write_log('yahoo', 'Initializing yahoo processer')
        self.choice = 'yahoo'
        self.timestamp = timestamp
        self.name = 'ygainers'
        self.headers = ['Symbol', 'Price', 'Change', 'Change %']

    def normalize(self):
        super().normalize()
        self.gainers_df.price = self.gainers_df.price.str.extract(r'(-?([0-9]*,)*[0-9]+.?[0-9]*)', expand = False)\
                .iloc[:, 0]\
                .str.replace(',', '')\
                .astype('float')
        self.gainers_df.price_percent_change = self.gainers_df.price_percent_change\
                .str.strip('+%')\
                .astype('float')
        self.gainers_df = self.gainers_df.sort_values('symbol')

        try:
            self.check()
            write_log('yahoo', 'gainers dataframe passed all formatting checks')
        except AssertionError as e:
            write_log('yahoo', 'e')
