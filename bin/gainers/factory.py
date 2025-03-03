from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f'Unrecognized source: {source}'
        self.choice = choice

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()

