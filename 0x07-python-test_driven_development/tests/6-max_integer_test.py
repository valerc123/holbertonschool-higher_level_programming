#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_tuple_int(self):
        self.assertRaises(TypeError, max_integer, ("hi", 2, 5))

    def test_tuple_str(self):
        self.assertAlmostEqual(max_integer(("Hello", "Holberton", "School")), "School")

    def test_float_list(self):
        self.assertAlmostEqual(max_integer([1.5, 4.3, 9.5]), 9.5)

    def test_empty(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_boolean(self):
        self.assertRaises(TypeError, max_integer, True)

    def test_string(self):
        self.assertAlmostEqual(max_integer("Holberton"), "t")

    def test_negative_num(self):
        self.assertAlmostEqual(max_integer([-2, -5, -1]), -1)

