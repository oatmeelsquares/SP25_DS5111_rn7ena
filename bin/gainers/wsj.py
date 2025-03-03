import requests
import pandas as pd
from yahoo import GainerDownload, GainerProcess
from abstractclasses import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.url = 'https://www.wsj.com/market-data/stocks/us/movers'

    def download(self):
        response = requests.get(self.url, headers = self.headers)
        assert response.status_code == 200, 'Failed to retreive wsj html'

        with open('wsjgainers.html', 'w') as wsjgainers_file:
            wsjgainers_file.write(response.text)

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        self.html = 'wsjgainers.html'

    def normalize(self):
        super().normalize()
        self.gainers_df.symbol = self.gainers_df.symbol.str.extract(r'\(([A-Z]{2,4})\)', expand = False)

        self.gainers_df = gainers_df
        self.check()

    def save_with_timestamp(self):
        super().save_with_timestamp()
        self.gainers_df.to_csv('wsjgainers.csv', index = False)





