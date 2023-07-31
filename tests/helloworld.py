import jpype
import jpype.imports

# jpype.startJVM()
import java     # noqa: E402
import javax    # noqa: E402

from javax.swing import JFrame, JLabel  # noqa: E402


def createAndShowGUI():
    frame = JFrame("HelloWorldSwing")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    label = JLabel("Hello World")
    frame.getContentPane().add(label)
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
