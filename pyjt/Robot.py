import time


class Robot:
    def __init__(self, robot=None):
        import java
        self._robot = robot if robot else java.awt.Robot()

    def move(self, control):
        position = control.getLocationOnScreen()
        self._robot.mouseMove(position.x, position.y)

    def click(self):
        import java
        self._robot.mousePress(java.awt.event.MouseEvent.BUTTON1_DOWN_MASK)
        time.sleep(0.05)
        self._robot.mouseRelease(java.awt.event.MouseEvent.BUTTON1_DOWN_MASK)
