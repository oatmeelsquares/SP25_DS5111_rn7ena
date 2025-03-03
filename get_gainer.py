import sys
sys.path.append('./bin/gainers/')
from base import ProcessGainer
from factory import GainerFactory

choice = sys.argv[1]

factory = GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

runner = ProcessGainer(downloader, normalizer)
runner.process()
