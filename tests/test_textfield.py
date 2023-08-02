from pyjt import FillMode


def test_type_textfield(helloworld, javax):
    tf1 = helloworld.locate(javax.swing.JTextField, name="tf1")
    assert tf1 is not None
    assert tf1.getText() == "textfield1"
    tf1.fill("Hello@World!$~_-()", mode=FillMode.TYPE)
    assert tf1.getText() == "Hello@World!$~_-()"


def test_set_textfield(helloworld, javax):
    tf2 = helloworld.locate(javax.swing.JTextField, text="tf2")
    tf2.fill("_Hello@World!$~", mode=FillMode.SET)
    assert tf2.getText() == "_Hello@World!$~"
