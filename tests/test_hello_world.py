from tdd_in_python import greeting


def test_greeting():
    assert greeting("World") == "Hello World!"
