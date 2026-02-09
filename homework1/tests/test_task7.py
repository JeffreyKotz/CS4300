"""
Task 6: File Handling
By Jeffrey Kotz - 2/8/2026

Test functionality of file handling in Task6.py
"""

import pytest
import numpy

from task7 import filter_containing_string

# Use parameterized test to test multiple sets of inputs
@pytest.mark.parametrize("names, string, expected_names", [
    (numpy.array(["test1", "test2", "test3", "test4"]), "test1", numpy.array(["test1"])), # exactly one name contains test1
    (numpy.array(["AAA", "AAB", "ABC", "BCD"]), "C", numpy.array(["ABC", "BCD"])),
    (numpy.array(["test1", "test2", "test3", "test4"]), "a", numpy.array([])), # No string contains a
    ])
def test_filter_containing_string(names: numpy.ndarray, string: str, expected_names: numpy.ndarray):
    """Test demonstration of the package numpy, to demonstrate numpy array filtering

    Args:
        names (numpy.ndarray): list of names being filtered
        string (str): string to filter for in the array of names
        expected_names (numpy.ndarray): names expected from filter
    """

    # Use numpy.array_equal() to compare the array to the expected resulting names
    assert numpy.array_equal(filter_containing_string(names, string), expected_names)
