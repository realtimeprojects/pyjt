import logging

from pyjt.Errors import ElementNotFoundError
from pyjt.ComponentFinder import Locator
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
        for window in wp.getWindows():
            if locator.matches(window):
                return Frame(window)
        raise ElementNotFoundError(f"Window {kwargs} not found!")

    @staticmethod
    def inspect():
        from java.awt import Window
        wp = Proxy(Window)
        result = []
        for window in wp.getWindows():
            result.append(Inspector.inspect(window))
        return result


class Frame(Fixture):
    def dispose(self):
        self._control.dispose()

    def close(self):
        from java.awt.event import WindowEvent
        self._control.instance.dispatchEvent(WindowEvent(self._component.instance, WindowEvent.WINDOW_CLOSING))
