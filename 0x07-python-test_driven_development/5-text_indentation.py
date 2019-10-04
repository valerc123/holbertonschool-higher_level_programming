#!/usr/bin/python3

"""This module prints a text
   with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    parameter text must be string
    """
    if type(text) is not str:
        raise TypeError("Text must be a string")
    if text is None:
        raise ValueError("Text is empty")
    flag = True
    for i in text:
        if flag and i is " ":
            continue
        print(i, end="")
        # if there are these characters in the text print two line breaks
        if i in ("?",".",":"):
            flag = True
            print()
            print()
        else:
            flag = False

