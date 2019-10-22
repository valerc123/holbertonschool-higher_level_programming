#!/usr/bin/python3
"""Module for base to test with unittest"""

import unittest
from models.base import Base


class Unittest_base(unittest.TestCase):
    """test for base clase"""
    def test_is_subclass(self):
        """ test instance """
        instance = Base(1)
        self.assertIsInstance(instance, Base)
        # Test that expresion is (or is not) None.
        self.assertIsNot(instance, Base)

    def test_id(self):
        """ test base ID """
        # id 2
        b1 = Base()
        # Test that first and second are equal
        self.assertEqual(b1.id, 3)
        self.assertEqual(b1.id, Base._Base__nb_objects)
        # id 12
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        # we didn't tested for integers
        b3 = Base("string")
        self.assertEqual(b3.id, "string")
        b4 = Base({id: 1})
        self.assertEqual(b4.id, {id: 1})
        # not a number
        # interpreted as a value
        # that is undefined or unrepresentable
        b5 = Base(float('NaN'))
        # a != b
        self.assertNotEqual(b5.id, b5.id)
        b6 = Base([2])
        self.assertEqual(b6.id, [2])
        b7 = Base(3.4)
        self.assertEqual(b7.id, 3.4)
        b8 = Base((3, 4))
        self.assertEqual(b8.id, (3, 4))
        b9 = Base({3, 4})
        self.assertEqual(b9.id, {3, 4})
        # id 2
        b10 = Base(None)
        self.assertEqual(b10.id, 2)
        self.assertEqual(b10.id, Base._Base__nb_objects)

    def test_module_docstring(self):
        """Tests docstring in class Base"""
        self.assertTrue(len(self.__class__.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests docstring in functions"""
        base = Base()
        self.assertTrue(len(base.to_json_string.__doc__) >= 1)

