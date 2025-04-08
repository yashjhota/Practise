from hello import add


def test_add():
    assert 2 == add(1, 1)


def test_add2():
    assert 3 == add(2, 1)
