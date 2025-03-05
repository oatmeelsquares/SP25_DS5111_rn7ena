import requests
import pandas as pd
from abstractclasses import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        self.url = 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'

    def download(self):
        response = requests.get(self.url, headers = self.headers)
        assert response.status_code == 200, f'Failed to retreive yahoo html: {response}'

        with open('ygainers.html', 'w') as ygainers_file:
            ygainers_file.write(response.text)

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
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

        self.check()
