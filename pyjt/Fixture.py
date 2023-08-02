import logging
from enum import Enum
from pyjt.Robot import Robot


log = logging.getLogger(__name__)

FillMode = Enum('FillMode', ['TYPE', 'SET', 'PASTE'])


class Fixture:
    def __init__(self, control):
        self._control = control
        self.robot = Robot()

    def click(self):
        log.debug(f"click({self._control})")
        self.robot.move(self._control)
        log.debug(f"executing click({self._control})")
        self.robot.click()

    def fill(self, text, mode=FillMode.TYPE, clear=True):
        """ Fill this control with the given **text**.

            :param text:    Text to fill this control with.
            :param mode:    Chosse the mode to fill the control with the
                            given text. See the table below.
            :param clear:   If set to true, select all text in the given control
                            before typing.

            ## Fill Modes

            -   FillMode.TYPE
                -   Fill the control by emulating keystrokes.
                -   Only supports US keyboard layout at this time.
            -   FillMode.SET
                -   Just set the text of the  component using the component.setText() function.
                -   The existing text is always overwritten ignoring the **clear** argument
            -   FillMode.PASTE
                -   Fill the control by pasting the text from the clipboard
                -   **Not implemented yet**
        """
        if mode == FillMode.TYPE:
            self.click()
            if clear:
                self._control.selectAll()
            self.robot.type(text)
        if mode == FillMode.SET:
            self._control.setText(text)

    def __getattr__(self, name):
        return getattr(self._control, name)
