import jpype
import jpype.imports

# jpype.startJVM()
import java     # noqa: E402
import javax    # noqa: E402

from javax.swing import JFrame, JLabel, JTextField  # noqa: E402
from java.awt import FlowLayout


def createAndShowGUI():
    frame = JFrame("HelloWorldSwing")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setBounds(10, 10, 500, 500)
    win = frame.getContentPane()
    win.setLayout(FlowLayout())
    label = JLabel("Hello World")
    win.add(label)
    tf1 = JTextField("textfield1")
    tf1.setName("tf1")
    tf1.setName("tf1")
    win.add(tf1)
    tf2 = JTextField("tf2")
    win.add(tf2)
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
