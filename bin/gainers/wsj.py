import os
import requests
import pandas as pd
from yahoo import GainerDownload, GainerProcess
from abstractclasses import GainerDownload, GainerProcess
from logger import write_log

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.choice = 'wsj'
        self.url = 'https://www.wsj.com/market-data/stocks/us/movers'
        write_log('wsj', f'Initializing wsj downloader with url {self.url}')

    def download(self):
        # for some reason, pandas couldn't find tables in the html from requests.get()
#        response = requests.get(self.url, headers = self.headers)
#        assert response.status_code == 200, 'Failed to retreive wsj html'
#
#        with open('wsjgainers.html', 'w') as wsjgainers_file:
#            wsjgainers_file.write(response.text)
        write_log('wsj', f'Retreiving html from {self.url}')
        status_code = os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html")
        if status_code:
            write_log('wsj', f'Error loading wsj html: {status_code}')
        else:
            write_log('wsj', 'Successfully loaded wsj html')

class GainerProcessWSJ(GainerProcess):
    def __init__(self, timestamp):
        write_log('wsj', 'Ititializing wsj processer')
        self.choice = 'wsj'
        self.name = 'wsjgainers'
        self.timestamp = timestamp
        self.headers = ['Unnamed: 0', 'Last', 'Chg', '% Chg']

    def normalize(self):
        super().normalize()
        self.gainers_df.symbol = self.gainers_df.symbol.str.extract(r'\(([A-Z\.]{2,5})\)', expand = False)

        try:
            self.check()
            write_log('wsj', 'gainers dataframe passed all formatting checks')
        except AssertionError as e:
            write_log('wsj', 'e')
