#!/usr/bin/python3
"""
Module that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence
    of '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    lines = text.splitlines()
    indented_lines = [line.strip() if line.strip() else "" for line in lines]

    indented_text = "\n".join(indented_lines)
    print(indented_text)
