"""
Task 6: File Handling
By Jeffrey Kotz - 2/8/2026

Test functionality of file handling in Task6.py
"""

import pytest

from task6 import count_words_in_file

def test_count_words_in_file():
    """test that the number of words in a file is properly counted
    """

    # File path of task6 read me text file
    FILE_PATH = "task6_read_me.txt"

    # I counted the number of words using notepad++ copying and pasting the text to have it count
    # The result was 104 words
    NUMBER_OF_WORDS = 104

    # If count_words_in_file produces the same number of words, it correctly counts the number of words
    # in the file
    assert count_words_in_file(FILE_PATH) == NUMBER_OF_WORDS