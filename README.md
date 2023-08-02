# pyjt - test java UI applications from python

pyjt supports you testing java UI applications from python.

Features:

-   Thread safe call of java ui components
-   Advanced locators to find ui compoments within the component tree
-   Simulate real user interactions by mouse and keyboard

This library makes use of **jpype** as the interface to the java
virtual machine. It basicaly consists of helper functions to
control the application from a test automation perspective.

## Quickstart

    import pyjt
    
    from javax.swing import JButton

    # start your java application here, in this case, we start
    # a hello world application located in HelloWorld.java
    pyjt.start(classpath="myapp/")
    pyjt.run("HelloWorld")

    # find the frame window titled "Hello World"
    frame = pyjt.FrameFinder.find(title="Hello World")

    # Locate and click a button on the frame
    frame.locate(JButton, text="Ok").click()

    # Locate and fill text to an text field
    frame.locate(JTextField, name="textfield1").fill("John Smith")

    # Close the frame (application)
    frame.close()

