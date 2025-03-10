from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from logger import write_log
from datetime import datetime

class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f'Unrecognized source: {choice}'
        self.choice = choice
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        write_log('factory', f"Initializing factory with choice '{choice}' at timestamp {self.timestamp}")

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo(self.timestamp)
        elif self.choice == 'wsj':
            return GainerProcessWSJ(self.timestamp)

