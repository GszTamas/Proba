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