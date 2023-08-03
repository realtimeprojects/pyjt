import pytest

# from pyjt import FrameFinder
import pyjt


@pytest.fixture(scope='session')
def jvm():
    pyjt.start(classpath="./")
    yield
    pyjt.stop()


@pytest.fixture(scope='session')
def java(jvm):
    import java
    return java


@pytest.fixture(scope='session')
def javax(jvm):
    import javax
    return javax


@pytest.fixture(scope='session')
def helloworld(jvm):
    import helloworld
    helloworld.main()
    window = pyjt.FrameFinder.find(title="HelloWorldSwing")
    yield window
    if window:
        window.dispose()
