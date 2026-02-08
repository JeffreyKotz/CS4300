"""
Task 2 Test
By Jeffrey Kotz - 2/7/2026
Test for task2 data type demonstrations
"""

import pytest

from task2 import integer_add, integer_div, float_div, float_mult, string_concat, string_print, bool_equals, bool_select


def test_integer_add():
    """test that integer_add properly demonstrations addition of integers
    """
    assert integer_add(3, 4) == 7

def test_integer_div():
    """test that integer_div properly demonstrates division of integers 
    """
    # result of 3/4 integer division will be zero as no decimal will be stored
    assert integer_div(3, 4) == 0

def test_float_mult():
    """test that float division is properly demonstrated
    """
    # pytest.approx() allows for approximating comparison of floating point values
    # 0.5 * 4.0 should equal 2.0
    assert float_mult(0.5, 4.0) == pytest.approx(2.0)


def test_float_div():
    """test that float division is properly demonstrated
    """
    # pytest.approx() allows for approximating comparison of floating point values
    # 5.0/2.0 should equal 2.5
    assert float_div(5.0, 2.0) == pytest.approx(2.5)


def test_string_concat():
    """test concatenation of strings
    """
    assert string_concat("abc", "def") == "abcdef"

def test_string_print(capsys):
    """test that string output is properly demonstrated

    Args:
        capsys: capsys provides capture of system stdout output
    """
    string_print("test")
    # capture output of test output
    output = capsys.readouterr()
    assert output.out == "test\n"

def test_bool_equals():
    """test that bool_equals functions properly
    """
    # If 2 and 2 are equal, 1 and 2 are not equal, test passes
    is_valid = bool_equals(2, 2) and (not bool_equals(1, 2))
    assert is_valid

def test_bool_select():
    """test that conditional selection based on a boolean value is properly demonstrated
    """
    is_valid = bool_select(2, 3, False) == 3 # test selection of 2nd value
    is_valid = is_valid and (bool_select(2, 3, True) == 2) # test selection of 3nd value

    # if both selections are correct, demonstration is valid
    assert is_valid
