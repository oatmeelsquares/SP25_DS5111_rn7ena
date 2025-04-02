import pytest
import sys
sys.path.append('/home/ubuntu/SP25_DS5111_rn7ena/bin/gainers') # ouch, this is something to look out for
# as a general rule 'no hard path coding'
# To point out the danger here, the 'ubuntu' in the path is not just because of the OS.  It also names the user.
# So in a work laptop that may be you, `/home/beckyd/` or something to that effect.
# the instance this code hits a machine, say in production where that path doesn't exist, this will break.
# So a better solution would be to use a relative path to where this executes from './bin/gainers/' for example

from factory import GainerFactory
from fixtures import choice

@pytest.mark.parametrize('gainer_factory_input',
                         ['website', 3, False,
                          'source', 'choice']
                         )
def test_init(gainer_factory_input):
    ''' make sure the factory will not initialize without a valid source.
        should throw AssertionError'''
    test_factory = None
    try:
        GainerFactory(gainer_factory_input)
    except Exception as e:
        assert isinstance(e, AssertionError), e
    
    if test_factory is not None: # if this succeeds, the test should fail
        assert False, 'GainerFactory initialized with invalid input'

def test_choice_downloader(choice):
    ''' make sure the factory returns a downloader of the correct type
        based on choice'''
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    
    assert f'gainerdownload{choice}' in str(type(downloader)).lower(), \
            f'GainerFactory returned the wrong downloader: {type(downloader)}'

def test_choice_processor(choice):
    ''' make sure the factory returns a processor of the correct type
        based on choice'''
    factory = GainerFactory(choice)
    processor = factory.get_processor()

    assert f'gainerprocess{choice}' in str(type(processor)).lower(), \
            f'GainerFactory returned the wrong processor: {type(processor)}'
