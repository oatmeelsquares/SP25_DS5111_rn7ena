import sys

def test_os():
    assert sys.platform == 'linux'

def test_version():
    good_versions = ['3.10', '3.11']
    assert sys.version[:4] in good_versions
