# test_factorial.py

import pytest
from factorial import calculate_factorial

def test_factorial_zero():
    """Factorial of 0 should be 1"""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Factorial of 1 should be 1"""
    assert calculate_factorial(1) == 1

def test_factorial_positive_small():
    """Factorial of 5 should be 120"""
    assert calculate_factorial(5) == 120

def test_factorial_positive_medium():
    """Factorial of 10 should be 3628800"""
    assert calculate_factorial(10) == 3628800

def test_factorial_large_number():
    """Factorial of 15 should be 1307674368000"""
    assert calculate_factorial(15) == 1307674368000

def test_factorial_negative_number():
    """Factorial of negative numbers should raise ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_negative_large():
    """Factorial of large negative numbers should raise ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-100)

def test_factorial_float_input():
    """Factorial of float numbers should raise TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)

def test_factorial_string_input():
    """Factorial of string input should raise TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")

def test_factorial_none_input():
    """Factorial of None should raise TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(None)
