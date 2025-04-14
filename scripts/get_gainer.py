import sys
sys.path.append('./bin/gainers/')
from base import ProcessGainer
from factory import GainerFactory
from datetime import datetime

choice = sys.argv[1]

def get_gainer(choice, timestamp = None):
    factory = GainerFactory(choice, timestamp)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    runner = ProcessGainer(downloader, normalizer)
    runner.process()

if choice == 'all':
    all_sources = ['yahoo', 'wsj']
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')

    for source in all_sources:
        get_gainer(source, timestamp)
else:
    get_gainer(choice)
    
