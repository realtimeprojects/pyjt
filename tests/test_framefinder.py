import pytest

from pyjt import FrameFinder


@pytest.fixture
def helloworld():
    import helloworld
    helloworld.main()
    window = FrameFinder.find(title="HelloWorldSwing")
    yield window
    if window:
        window.close()


def test_find_frame(helloworld):
    assert helloworld is not None
