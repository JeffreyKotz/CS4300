"""
Task 1 Test
By Jeffrey Kotz - 2/7/2026
Test for task1 for valid hello world output to console.
"""

import pytest

from task1 import hello_world

def test_hello_world(capsys):
    """test that the hello_world function produces proper output to stdout ("Hello, World!")

    Args:
        capsys: capsys provides capture of system output for the sake of testing output
    """

    hello_world()
    # capture stdout output from helloworld
    output = capsys.readouterr()
    # Assert the result of comparison between the actual output and desired result
    assert output.out == "Hello, World!\n"
