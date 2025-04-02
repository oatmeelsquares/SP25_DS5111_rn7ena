import sys

def test_os():
    assert sys.platform == 'linux'

def test_version():
    good_versions = ['3.10', '3.11'] # will have to update to match changes in validation.yml.  By the way, your AWS vm also uses 3.12, right?
    assert sys.version[:4] in good_versions
