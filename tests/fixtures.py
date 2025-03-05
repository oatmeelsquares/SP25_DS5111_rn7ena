import pytest

@pytest.fixture(params = ['wsj', 'yahoo'])
def choice(request):
    return request.param
