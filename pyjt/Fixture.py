import logging
from enum import Enum
from pyjt.Robot import Robot
from pyjt.ComponentFinder import ComponentFinder, Locator
from pyjt.Errors import ElementNotFoundError

log = logging.getLogger(__name__)

FillMode = Enum('FillMode', ['TYPE', 'SET', 'PASTE'])


class Fixture:
    """ Wrapper class to control a specific UI element.
    """
    def __init__(self, control):
        self._control = control
        self.robot = Robot()

    def locate(self, locator=None, **kwargs):
        """ Search a control as a sub-element of the control
            managed by this fixture.

            Parameters
            ----------

            locator:    Locator
                A locator object to find the sub-control
            **kwargs:
                Additional search parameters.
        """
        log.debug(f"frame.find({locator}, {kwargs})")
        locator = locator if locator else Locator(**kwargs)
        control = ComponentFinder.findIn(self._control.getComponents, locator)
        if not control:
            raise ElementNotFoundError(f"Control({kwargs}) not found!")
        return Fixture(control)

    def find(self, role, **kwargs):
        kwargs['role'] = role
        return self.locate(**kwargs)

    def click(self):
        """ Move the mouse over this control and execute a click. """
        log.debug(f"click({self._control})")
        self.robot.move(self._control)
        log.debug(f"executing click({self._control})")
        self.robot.click()

    def fill(self, text, mode=FillMode.TYPE, clear=True):
        """ Fill this control with the given **text**.

            Args:
                text:   Text to fill this control with.
                mode:   FillMode - Choose the mode to fill the control with the given text.
                        See the table below.
                clear:  If set to True, select all text in the given control
                        before typing.

            FillMode:

                FillMode.TYPE:
                  - Fill the control by emulating keystrokes.
                  - Only supports US keyboard layout at this time.
                FillMode.SET:
                  -   Just set the text of the  component using the component.setText() function.
                  -   The existing text is always overwritten ignoring the **clear** argument
                FillMode.PASTE:
                  - Fill the control by pasting the text from the clipboard
                  - **Not implemented yet**

        """
        if mode == FillMode.TYPE:
            self.click()
            if clear:
                self.robot.selectAll()
            self.robot.type(text)
        if mode == FillMode.SET:
            self._control.setText(text)

    def __getattr__(self, name):
        return getattr(self._control, name)

    def __repr__(self):
        return str(self._control)
