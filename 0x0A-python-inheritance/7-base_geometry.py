#!/usr/bin/python3
'''
    Module - BaseGeometry
'''


class BaseGeometry:
    '''
    BaseGeometry class
    '''
    def area(self):
        ''' Raise error Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates value

        Parameters
        name: string name
        value: value, should be an integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
