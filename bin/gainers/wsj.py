import os
import requests
import pandas as pd
from yahoo import GainerDownload, GainerProcess
from abstractclasses import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.url = 'https://www.wsj.com/market-data/stocks/us/movers'

    def download(self):
        # for some reason, pandas couldn't find tables in the html from requests.get()
#        response = requests.get(self.url, headers = self.headers)
#        assert response.status_code == 200, 'Failed to retreive wsj html'
#
#        with open('wsjgainers.html', 'w') as wsjgainers_file:
#            wsjgainers_file.write(response.text)
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html")

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        self.name = 'wsjgainers'
        self.headers = ['Unnamed: 0', 'Last', 'Chg', '% Chg']

    def normalize(self):
        super().normalize()
        self.gainers_df.symbol = self.gainers_df.symbol.str.extract(r'\(([A-Z\.]{2,5})\)', expand = False)

        self.check()
