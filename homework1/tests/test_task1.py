"""
By Jeffrey Kotz - 2026
Test for task1 for valid output
"""

from task1 import hello_world

def test_hello_world(capsys):
    """
    Test that task1 produces the output "Hello, World!"

    :param capsys: parameter allowing stdout and stderr to be captured and read
    """

    hello_world()
    output = capsys.readouterr() # capture stdout output from hellowrold
    assert output.out == "Hello, World!\n" # Assert the result of comparison between the actual output and desired result