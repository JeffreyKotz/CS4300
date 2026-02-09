"""
Task 6: File Handling
By Jeffrey Kotz - 2/8/2026

Demonstrate File handling and operations
"""

def count_words_in_file(file_path: str) -> int:
    """count the number of words in a file of a given file name

    Args:
        file_path (str): name/relative path of file

    Returns:
        int: count of all words in the given file
    """

    count = -1

    with open(file_path, "r") as file:
        # Read full text of file
        file_text = file.read()

        # split file text string into a list using split() method
        # split() with no arguments by default splits string delimited
        # by any white space character space, newline, etc/
        # https://www.w3schools.com/python/ref_string_split.asp
        words = file_text.split()

        # The number of words is equal to the number of elements in the list
        count = len(words)

    return count

if __name__ == "__main__":

    # Name of file used
    # THIS FILE PATH ASSUMES SCRIPT IS RUN FROM homework1/ directory, not homework1/src
    FILE_PATH = "task6_read_me.txt"

    print("Demonstration: File Handling - By Jeffrey Kotz")

    word_count = count_words_in_file(FILE_PATH)

    print(f"Number of words inside file task6_read_me.txt: {word_count} words\n")

    # file read is one level outside of src directory, relative path is given
