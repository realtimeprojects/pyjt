""" Find and control a frame.
"""
import logging

from pyjt.Errors import ElementNotFoundError
from pyjt.ComponentFinder import Locator
from pyjt.Fixture import Fixture
from pyjt.Inspector import Inspector
from pyjt import Proxy

log = logging.getLogger(__name__)


class FrameFinder:
    """ Helper class to find a frame in the list of application frames.
    """
    @staticmethod
    def find(locator=None, **kwargs):
        """ Find a frame by a **locator or frame attributes.

            :param locator: Locator to find a frame
            :param kwargs:  Frame attributes.
        """
        from java.awt import Window
        locator = locator if locator else Locator(**kwargs)
        wp = Proxy(Window)
        for window in wp.getWindows():
            if locator.matches(window):
                return Frame(window)
        raise ElementNotFoundError(f"Window {kwargs} not found!")

    @staticmethod
    def inspect():
        """ :return: A dicitionary tree of all ui components of all available
            frames.
        """
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
