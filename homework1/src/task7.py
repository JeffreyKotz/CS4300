"""
Task 7: Package Managment
By Jeffrey Kotz - 2/8/2026

Demonstration of package managment using the numpy package
"""

# My chosen package is numpy a useful package for mathematical operations
import numpy

def filter_containing_string(names: numpy.ndarray, string: str) -> numpy.ndarray:
    """_summary_

    Args:
        names (ndarray): numpy array to return filter of
        string (str): string to search for in names

    Returns:
        ndarray: filtered array of only elements containing the given string
    """

    # filter list, to be applied to array to obtain filtered values
    filter = []

    # filter names array for only values containing the given string
    # if name contains string append True to the filter list, else append false
    # True indicating that a value is kept, false to discard when filtering
    for name in names:
        if (string in name):
            filter.append(True)
        else:
            filter.append(False)
    
    # return the names array with the filter applied
    return names[filter]


if __name__ == "__main__":
    print("Demonstration: Package Management (Using NumPy) - By Jeffrey Kotz")

    print("""\nA useful feature of NumPy, is that NumPy provides arrays data structure with contiguous memory.
Numpy provides various useful features for arrays such as the ability to filter arrays using
filter list of bools to obtain specific values of the array. Useful when trying to identify,
 sort, or search for specific entries in a large amount of data given a set of parameters.
""")

    # example names for demonstration
    names = numpy.array(["Jeffrey", "James", "Alex", "Dave", "Chester", "Pat"])

    print(f"For example given the array of names: {names}")
    print("We could use NumPy to filter for specific names by first building a list for all names matching our set condition.")

    print(f"We could filter for all names that contain an 'a': {filter_containing_string(names, "a")}")
    print(f"Or for names that contain 'Test': {filter_containing_string(names, "Test")}")
    print(f"Or for names that contain 'J': {filter_containing_string(names, "J")}\n")