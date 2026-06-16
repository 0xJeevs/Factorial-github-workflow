# test_factorial.py

import pytest
from factorial import calculate_factorial

def test_factorial_positive():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6
    assert calculate_factorial(1) == 1

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        calculate_factorial(-5)

def test_factorial_invalid_type():
    with pytest.raises(TypeError, match="Input must be an integer."):
        calculate_factorial(3.14)
    with pytest.raises(TypeError, match="Input must be an integer."):
        calculate_factorial("five")
