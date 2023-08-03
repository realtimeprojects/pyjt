import jpype
import jpype.imports

# jpype.startJVM()
import java     # noqa: E402
import javax    # noqa: E402

from javax.swing import JFrame, JLabel, JTextField, BoxLayout  # noqa: E402
from java.awt import Container


class LabeledTextField:
    def __init__(self, name=None, label=None, text=None):
        self._label = JLabel(label)
        self._textfield = JTextField(text)
        self._container = Container()
        if name:
            self._container.setName(name)
        self._container.setLayout(BoxLayout(self._container, BoxLayout.PAGE_AXIS))
        self._container.add(self._label)
        self._container.add(self._textfield)

    def addTo(self, container):
        container.add(self._container)


def createAndShowGUI():
    frame = JFrame("HelloWorldSwing")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setBounds(10, 10, 500, 500)
    win = frame.getContentPane()
    win.setLayout(BoxLayout(win, BoxLayout.PAGE_AXIS))
    label = JLabel("Hello World")
    win.add(label)
    tf1 = JTextField("textfield1")
    tf1.setName("tf1")
    tf1.setName("tf1")
    win.add(tf1)
    tf2 = JTextField("tf2")
    win.add(tf2)
    ltf3 = LabeledTextField(label="Name:", text="textfield3")
    ltf3.addTo(win)
    ltf4 = LabeledTextField(label="Email:", text="textfield4")
    ltf4.addTo(win)
    frame.pack()
    frame.setVisible(True)


# Start an event loop thread to handling gui events
@jpype.JImplements(java.lang.Runnable)
class Launch:
    @jpype.JOverride
    def run(self):
        createAndShowGUI()


def main():
    javax.swing.SwingUtilities.invokeLater(Launch())


if __name__ == "__main__":
    main()
