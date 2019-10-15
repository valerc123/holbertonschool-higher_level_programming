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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
