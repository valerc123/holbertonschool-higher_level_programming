#!/usr/bin/python3
'''
    Module - number_of_lines
'''


def number_of_lines(filename=""):
    '''
    Function that returns the number of lines of a text file
    '''
    with open(filename, 'r', encoding='utf8') as f:
        i = 0
        for lines in f:
            i += 1
        return i
