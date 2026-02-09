"""
Task 2 Test
By Jeffrey Kotz - 2/7/2026
Test for task2 data type demonstrations
"""

import pytest

from task2 import integer_add, integer_div, float_div, float_mult, string_concat, string_print, bool_equals, bool_select

# Parameterized test used to test multiple values
@pytest.mark.parametrize("x, y, expected_result", [(1, 2, 3), (3, 4, 7), (5, 5, 10)])
def test_integer_add(x, y, expected_result):
    """Test that integer_add properly demonstrations addition of integers.

    Args:
        x (int): first integer to add
        y (int): second integer being added
        expected_result (int): expected result of x + y
    """
    assert integer_add(x, y) == expected_result

# Parameterized test used to test multiple values for integer division
@pytest.mark.parametrize("x, y, expected_result", [(2, 3, 0), (4, 2, 2), (-5, 2, -2)])
def test_integer_div(x, y, expected_result):
    """Test that integer_div properly demonstrates division of integers.

    Args:
        x (int): divisor
        y (int): divident
        expected_result (int): expected quotient of x/y
    """
    assert integer_div(x, y) == expected_result

# Parameterized test used to test multiple values for floating point multiplication
@pytest.mark.parametrize("x, y, expected_result", [(2.5, 2.5, 6.25), (0.5, 5.0, 2.5), (-1.0, 10.5, -10.5)])
def test_float_mult(x, y, expected_result):
    """Test that float division is properly demonstrated.

    Args:
        x (float): first value to multiply
        y (float): second value to multiply
        expected_result (float): expected result of x*y
    """
    # pytest.approx() allows for approximating comparison of floating point values
    # accounting for floating point error
    assert float_mult(x, y) == pytest.approx(expected_result)


# Parameterized test used to test multiple sets of values for floating point division
@pytest.mark.parametrize("x, y, expected_result", [(5.0, 2.0, 2.5), (1.0, 5.0, 0.2), (9.0, 2, 4.5)])
def test_float_div(x, y, expected_result):
    """Test that float division is properly demonstrated.

    Args:
        x (float): divisor
        y (float): divident
        expected_result (float): expected quotient of x/y
    """
    # pytest.approx() allows for approximating comparison of floating point values
    # 5.0/2.0 should equal 2.5
    assert float_div(x, y) == pytest.approx(expected_result)


# Parameterized test used to test multiple sets of strings for concatenation
@pytest.mark.parametrize("string1, string2, combined_string", [("abc", "def", "abcdef"), ("Hello, ", "World!", "Hello, World!"), ("This is ", "a test!", "This is a test!")])
def test_string_concat(string1, string2, combined_string):
    """Test concatenation of strings.

    Args:
        string1 (str): first string to be concatenated
        string2 (str): second string concatenated to end of first
        combined_string (str): combined result of string1 and string2
    """
    assert string_concat(string1, string2) == combined_string

# Parameterize input to string_print test, to test multiple string literals
@pytest.mark.parametrize("string", [("abc"), ("Hello, World!"), ("This is a test!")])
def test_string_print(capsys, string):
    """test that string output is properly demonstrated

    Args:
        capsys: capsys provides capture of system stdout output
        string (str): string being printed by string_print()
    """
    string_print(string)
    # capture output of test output
    output = capsys.readouterr()
    assert output.out == string + "\n" # newline is added when a string is printed

# Test bool_equals with multiple sets of parameters to ensure cohesive testing of boolean operations
@pytest.mark.parametrize("x, y, expected_result", [(1, 98, False), (2, 2, True), (3, -3, False), (0, 0, True)])
def test_bool_equals(x, y, expected_result):
    """Test that bool_equals functions properly compares equality

    Args:
        x (int): first value compared
        y (int): second value compared
        expected_result (bool): boolean result of comparing x and y for equality
    """
    # If the equality test of x and y matches the expected_result the test passes
    assert bool_equals(x, y) == expected_result

# Parameterize test, to ensure that using a boolean flag to select between two values properly functions
@pytest.mark.parametrize("x, y, choose_first_flag, expected_result", [(1, 98, False, 98), (1, 98, True, 1), (3, -3, False, -3), (0, -1, True, 0)])
def test_bool_select(x, y, choose_first_flag, expected_result):
    """Test that conditional selection based on a boolean value is properly demonstrated.

    Args:
        x (int): first value
        y (int): second value
        choose_first_flag (bool): boolean flag used to select x if true, y if false
        expected_result (int): the expected result with the given parameters
    """
    # If the selection chooses the correct value, the test passes
    assert bool_select(x, y, choose_first_flag) == expected_result
