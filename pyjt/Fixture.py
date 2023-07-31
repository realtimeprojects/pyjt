from pyjt.Robot import Robot
import logging

log = logging.getLogger(__name__)


class Fixture:
    def __init__(self, control):
        self._control = control

    def click(self):
        log.debug(f"click({self._control})")
        robot = Robot()
        robot.move(self._control)
        robot.click()

    def fill(self, text):
        self.click()
        self._control.setText(text)

    def __getattr__(self, name):
        return getattr(self._control, name)
