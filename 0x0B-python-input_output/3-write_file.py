#!/usr/bin/python
'''
    Module - write_file
'''


def write_file(filename="", text=""):
    '''Function that writes a string to a text file (UTF8) and
     returns the number of characters written
    '''
    with open(filename, 'w', encoding='utf8') as f:
        num_characters = f.write(text)
    return num_characters
