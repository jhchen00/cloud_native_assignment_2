import src.main

def test_add():
    assert src.main.add(3, 21) == 24
    assert src.main.add(-1, 9) == 8

def test_subtract():
    assert src.main.subtract(5, 8) == -3
    assert src.main.subtract(-1, 6) == -7

def test_multiply():
    assert src.main.multiply(3, 3) == 9
    assert src.main.multiply(100, 0) == 0
    assert src.main.multiply(-2, 5) == -10

def test_fibonacci():
    assert src.main.fibonacci(0) == 0
    assert src.main.fibonacci(1) == 1
    assert src.main.fibonacci(10) == 55