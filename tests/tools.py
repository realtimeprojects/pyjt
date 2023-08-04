

def assert_raises(exception, func):
    try:
        func()
    except exception:
        return
    assert f"{exception} not raised"
