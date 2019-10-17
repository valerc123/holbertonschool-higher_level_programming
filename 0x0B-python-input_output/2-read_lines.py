#!/usr/bin/python3
'''
    Module - read_lines
'''


def read_lines(filename="", nb_lines=0):
    '''
    Function that reads n lines of a text file (UTF8) and prints it to stdout

    Parameters:
        filename: String with the name of the file
        nb_lines: number of lines to be read
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            total_lines = 0
            for lines in f:
                total_lines += 1
                print(lines, end="")
                if total_lines == nb_lines:
                    break
