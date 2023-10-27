import pytest

# from pyjt import FrameFinder
import pyjt


@pytest.fixture(scope='session')
def jvm():
    pyjt.start("-Xmx512m", "-Xmx4G", classpath="./")
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
    helloworld.main("HelloWorldSwing")
    window = pyjt.FrameFinder.find(title="HelloWorldSwing")
    window.setDefaultCloseOperation(window.DISPOSE_ON_CLOSE)
    yield window
    if window:
        window.dispose()


@pytest.fixture()
def hwlocal(jvm):
    import helloworld
    helloworld.main("hwlocal")
    window = pyjt.FrameFinder.find(title="hwlocal")
    window.setDefaultCloseOperation(window.DISPOSE_ON_CLOSE)
    yield window
    if window:
        window.dispose()
