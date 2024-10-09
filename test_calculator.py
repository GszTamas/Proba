import pytest
from calculator import *

def test_sum():
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 2) == 1
    assert calculate_sum(-1, -2) == -3
    assert calculate_sum(0, 0) == 0

def test_substraction():
    assert calculate_substraction(5, 2) == 3
    assert calculate_substraction(-1, 2) == -3
    assert calculate_substraction(-1, -2) == 1
    assert calculate_substraction(0, 0) == 0

def test_multiplication():
    assert calculate_multiplication(5, 2) == 10
    assert calculate_multiplication(-1, 2) == -2
    assert calculate_multiplication(-1, -2) == 2
    assert calculate_multiplication(0, 0) == 0

def test_division():
    assert calculate_division(4, 2) == 2
    assert calculate_division(-1, 2) == -0.5
    assert calculate_division(-1, -2) == 0.5
    assert calculate_division(0, 0) == "error"