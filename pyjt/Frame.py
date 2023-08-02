import logging

from pyjt.Errors import ElementNotFoundError
from pyjt.ComponentFinder import ComponentFinder, Locator
from pyjt.Fixture import Fixture
from pyjt.Inspector import Inspector
from pyjt import Proxy

log = logging.getLogger(__name__)


class FrameFinder:
    @staticmethod
    def find(locator=None, **kwargs):
        from java.awt import Window
        locator = locator if locator else Locator(**kwargs)
        wp = Proxy(Window)
        window = ComponentFinder.findIn(func=wp.getWindows, locator=locator)
        if not window:
            raise ElementNotFoundError(f"Window {kwargs} not found!")
        return Frame(window=window)

    @staticmethod
    def inspect():
        from java.awt import Window
        wp = Proxy(Window)
        result = []
        for window in wp.getWindows():
            result.append(Inspector.inspect(window))
        return result


class Frame:
    def __init__(self, window=None):
        self._window = window

    def find(self, locator=None, **kwargs):
        log.debug(f"frame.find({locator}, {kwargs})")
        locator = locator if locator else Locator(**kwargs)
        control = ComponentFinder.find(self._window, locator)
        if not control:
            raise ElementNotFoundError(f"Control({kwargs}) not found!")
        return Fixture(control)

    def locate(self, role, **kwargs):
        kwargs['role'] = role
        return self.find(**kwargs)

    def dispose(self):
        self._window.dispose()

    def close(self):
        from java.awt.event import WindowEvent
        self._window.instance.dispatchEvent(WindowEvent(self._window.instance, WindowEvent.WINDOW_CLOSING))
