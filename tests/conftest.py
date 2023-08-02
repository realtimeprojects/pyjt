import pytest

# from pyjt import FrameFinder
import pyjt


@pytest.fixture
def helloworld(scope='session'):
    pyjt.start()
    import helloworld
    helloworld.main()
    window = pyjt.FrameFinder.find(title="HelloWorldSwing")
    yield window
    if window:
        window.close()
