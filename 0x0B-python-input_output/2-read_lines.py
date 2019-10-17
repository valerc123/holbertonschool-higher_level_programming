#!/usr/bin/python3
'''
    Module - read_lines
'''


def read_lines(filename="", nb_lines=0):
    '''
    Function that reads n lines of a text file (UTF8) and prints it to stdout
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        total_lines = 0
        for total_lines, lines in enumerate(f):
            print(lines, end="")
            if total_lines == nb_lines:
                    break
            print(lines, end="")
