"""
Task 4: Functions and Duck Typing
By Jeffrey Kotz - 2/7/2026

Demonstrate use of duck typing in functions
"""

import pytest

from task4 import calculate_discount

def test_calculate_discount_ints():
    """test calculate discount with just integer values
    """
    assert calculate_discount(50, 50) == "$25.00"

def test_calculate_discount_int_float():
    """test calculate discount with price of integer, and discount percent of float
    """
    assert calculate_discount(50, 12.50) == "$43.75"

def test_calculate_discount_float_int():
    """test calculate discount with price of float, and discount percent of integer
    """
    assert calculate_discount(75.50, 50) == "$37.75"

def test_calculate_discount_floats():
    """test calculate discount with just floating point values
    """
    assert calculate_discount(20.50, 25.25) == "$15.32"