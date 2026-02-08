"""
Task 3 Test
By Jeffrey Kotz - 2/7/2026
Test for task3 control structure demonstrations
"""

import pytest

from task3 import sign_of, print_first_n_primes, sum_one_to_n


### sign_of tests - if control structure
def test_sign_of_positive():
    """test that sign_of uses if statements properly to determine sign of positive values.
    """
    assert sign_of(3) == "positive"

def test_sign_of_negative():
    """test that sign_of uses if statements properly to determine sign of negative values.
    """
    assert sign_of(-3) == "negative"

def test_sign_of_zero():
    """test that sign_of uses if statements properly to determine sign of zero.
    """
    assert sign_of(0) == "zero"

### print_first_n_primes - for control structure
def test_print_first_n_primes(capsys):
    """test that first n primes are properly calculated, in this case 10 primes.

    Args:
        capsys: capsys allows for capture of system output for validity comparison
    """
    # the first 10 primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    print_first_n_primes(10)

    # Read output
    output = capsys.readouterr()
    assert output.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

### summation of one to one hundred - while control structure verification
def test_sum_one_to_n():
    """test than summation from 1 to 100 is valid using the while control strcuture
    """
    assert sum_one_to_n(100) == 5050 # the sum of 1 to 100 us 5050
