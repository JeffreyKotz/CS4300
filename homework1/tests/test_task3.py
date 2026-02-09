"""
Task 3 Test
By Jeffrey Kotz - 2/7/2026
Test for task3 control structure demonstrations
"""

import pytest

from task3 import sign_of, print_first_n_primes, sum_one_to_n


### sign_of tests - if control structure
# Parameterized test, ensuring all edge cases are met (negatives, zero, positive)
@pytest.mark.parametrize("n, expected_result", [(-5, "negative"), (0, "zero"), (5, "positive"), (0.0001, "positive"), (-0.001, "negative"), (-5.0, "negative"), (5.0, "positive")])
def test_sign_of(n, expected_result):
    """Test that sign_of uses if statements properly to determine sign of of a numeric value properly.

    Args:
        n (number): any number n to find the sign of using an if statement
        expected_result (str): a string representing whether the number is positive, negative, or zero
    """
    assert sign_of(n) == expected_result

### print_first_n_primes - for control structure
# Parameterize test, ensuring edge cases are met
# nothing should be printed for values of n <1, and values >0 should properly output the values up to n
@pytest.mark.parametrize("n, expected_result", [(5, "2\n3\n5\n7\n11\n"), (0, ""), (-1, ""), (10, "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n")])
def test_print_first_n_primes(capsys, n, expected_result):
    """test that first n primes are properly calculated, in this case 10 primes.

    Args:
        capsys: capsys allows for capture of system output for validity comparison
    """
    # the first 10 primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    print_first_n_primes(n)

    # Read output
    output = capsys.readouterr()
    assert output.out == expected_result

### summation of one to one hundred - while control structure verification
# Using parameterized tests to test edge cases, valeus >=1 should give proper sum output
# values <1 should return 0 as the summation starts at 1, after the value give
@pytest.mark.parametrize("n, expected_result", [(5, 15), (100, 5050), (0, 0), (-3, 0), (1, 1)])
def test_sum_one_to_n(n, expected_result):
    """Test than summation from 1 to n is valid using the while control strcuture

    Args:
        n (int): value to sum to starting from 1
        expected_result (int): expected result of summation
    """
    assert sum_one_to_n(n) == expected_result
