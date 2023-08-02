from pyjt import FillMode


def test_find_type_textfield(helloworld):
    tf1 = helloworld.find(name="tf1")
    assert tf1 is not None
    assert tf1.getText() == "textfield1"
    tf1.fill("Hello@World!", mode=FillMode.TYPE)
    assert tf1.getText() == "Hello@World!"
    tf1.fill("World", mode=FillMode.SET)
    assert tf1.getText() == "World"
