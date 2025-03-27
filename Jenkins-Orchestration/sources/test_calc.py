import pytest
from calc import add2

def test_add2_numeric():
    assert add2(1, 2) == 3
    assert add2(-1, 1) == 0
    assert add2(0, 0) == 0

def test_add2_string():
    assert add2("hello", "world") == "helloworld"
    assert add2("", "") == ""
    assert add2("a", "b") == "ab"

def test_add2_mixed():
    assert add2("hello", 123) == "hello123"
    assert add2(123, "hello") == "123hello"
    assert add2("number", 42) == "number42" 