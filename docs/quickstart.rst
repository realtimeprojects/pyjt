Quickstart
==========

Installation
------------

Install pyjt using pip3:

.. code:: bash

    pip3 install pyjt

Starting your app and identifying a frame
-----------------------------------------

pyjt uses `jpype <https://github.com/jpype-project/jpype>`_ to start a JVM inside your python
thread and starts your application inside this JVM.

Create a python script named ``sample.py`` and add the following code:

.. code:: python

    import pyjt

    # start the JVM
    pyjt.start()

Now you can run your application using ``pyjt.run()``. pyjt
expects the name of the class of your application containing
a ``main()`` function and it will run the main function:

.. code:: python

    pyjt.run("MyApplication")

Now you can use the `FrameFinder` to identify your frame, e.g.
by the title:

.. code:: python

    frame = pyjt.FrameFinder.find(title="Hello World")

The simplest thing to do is to close your application now from pyjt:

.. code:: python

   frame.close()

Locate and check UI elements
----------------------------

Once you found your frame, you can use the ``find()`` function
to locate UI elements in your frame. The code below
tries to find a ``JTextField`` control with the name ``firstname``
and reads out and checks the text of this field. All calls
to the components are handled in the JVM event thread to ensure
thread safety:

.. code:: python

   firstname = frame.find(JTextField, name='first name')
   assert firstname.getText() == 'John'

Control UI elements
-------------------

You can now use the ``fill()`` function to set the
text of the textfield:

.. code:: python

   firstname.fill("Johnny")
