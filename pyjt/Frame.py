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
        """Find a frame by a locator or frame attributes.

        Parameters
        ----------
        locator : Locator
            Locator to find a frame.
        **kwargs :
            Search filters by keyword arguments.

        Raises
        ------

        ElementNotFoundError
            If the no frame was found matching the given search criteria.

        Returns
        -------
        Frame
            A Frame instance reflecting the frame window found by the find
            operation.
        """
        from java.awt import Window
        locator = locator if locator else Locator(**kwargs)
        wp = Proxy(Window)
        for window in wp.getWindows():
            if locator.matches(window):
                return Frame(window)
        raise ElementNotFoundError(f"Window {locator} not found!")

    @staticmethod
    def inspect():
        """ Inspect a component

            Returns
            -------

            dict    A dicitionary tree of all ui components of all available
                    frames.
        """
        from java.awt import Window
        wp = Proxy(Window)
        result = []
        for window in wp.getWindows():
            result.append(Inspector.inspect(window))
        return result


class Frame(Fixture):
    """ Wrapper for controlling a frame. """
    def dispose(self):
        """ Dispose this frame. """
        self._control.dispose()

    def close(self):
        """ Close this frame by sending a close message. """
        from java.awt.event import WindowEvent
        self._control.instance.dispatchEvent(WindowEvent(self._component.instance, WindowEvent.WINDOW_CLOSING))
