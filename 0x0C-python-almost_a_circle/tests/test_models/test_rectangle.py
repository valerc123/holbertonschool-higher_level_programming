#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_classBase(self):
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)
        self.assertIsInstance(r, Rectangle)

    def test_class(self):
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Base))

    def test_subclass(self):
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Rectangle))

    def test_width_neg(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -1, 1)
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_rectangle_noargs(self):
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_one_arg(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_instance(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Rectangle)

    def test_rectangle_inherits_base(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Base)

    def test_rectangle_defaults(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
