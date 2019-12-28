import pytest
import function

def test_none():
    assert function.sum_numbers(None) == None

def test_error():
    with pytest.raises(TypeError):
        function.sum_numbers('a')

def test_custom():
    assert function.sum_numbers(-5) == 0
    assert function.sum_numbers(0) == 0
    assert function.sum_numbers(5) == 15
