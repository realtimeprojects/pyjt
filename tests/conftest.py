import pytest

# from pyjt import FrameFinder
import pyjt


@pytest.fixture(scope='session')
def helloworld():
    pyjt.start()
    import helloworld
    helloworld.main()
    window = pyjt.FrameFinder.find(title="HelloWorldSwing")
    yield window
    if window:
        window.dispose()
    pyjt.stop()
