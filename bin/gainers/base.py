from logger import write_log

class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):

        success = False
        while success == False:
            try:
                self._download()
                self._normalize()
                success = True
            except ValueError as v:
                write_log(self.downloader.choice, f'Failed to parse tables: {v}.\nTrying again...')

        self._save_to_file()
