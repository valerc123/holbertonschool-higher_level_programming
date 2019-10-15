#!/usr/bin/python3
'''
    Module - BaseGeometry
'''


class BaseGeometry:
    ''' class BaseGeometry'''
    def area(self):
        ''' Raise error Exception'''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
