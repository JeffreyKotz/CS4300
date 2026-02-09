"""
Task 4: Functions and Duck Typing
By Jeffrey Kotz - 2/7/2026

Demonstrate use of duck typing in functions
"""

import pytest

from task4 import calculate_discount


@pytest.mark.parametrize("price, discount, expected_result",
    [(50, 50, "$25.00"), # Test with just integers
    (50, 12.50, "$43.75"), # Test with int price, float discount
    (75.50, 50, "$37.75"), # Test with float price, int discount
    (20.50, 25.25, "$15.32"), # Test with just floats
    (-1, 50, "$-1.00"), # test with invalid price <0, error is printed and result is a negative price to reflect
    (50, -1, "$-1.00"), # test with invalid discount <0, error is printed and result is negative price
    (50, 101, "$-1.00"), # test with invalid discount >100, can't have more than 100% off a price
    ])
    
def test_calculate_discount_ints(price, discount, expected_result):
    """test calculate discount with just integer values
    """
    assert calculate_discount(price, discount) == expected_result
