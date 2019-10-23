#!/usr/bin/python3
""" 
TestBase - To prube the class base
"""
import unittest
from models.base import Base


class Unittest_base(unittest.TestCase):
    def setUp(self):
        """
        setUp - set up the private value
        __nb_objects = 0
        """
        Base._Base__nb_objects = 0
    def test_id(self):
        """
        test_id - test the id
        """
        in_1 = Base()
        self.assertEqual(in_1.id, 1)
        
    def test_instance(self):
        """
        test_instance - test the instance id
        """
        in_1 = Base()
        in_2 = Base()
        in_3 = Base()
        in_4 = Base()
        in_5 = Base()
        in_6 = Base()
        in_7 = Base()
        in_8 = Base()
        in_9 = Base()
        self.assertEqual(in_9.id, 9)
    
    def test_id_value(self):
        """
        test_id_value - change the id
        """
        in_1 = Base(15)
        self.assertEqual(in_1.id, 15)
    
    def test_negative_number(self):
        """
        test_negative_number - change
        the id for negative number
        """
        in_1 = Base(-1)
        self.assertEqual(in_1.id, -1)
    
    def test_string(self):
        """
        test_string - change the id for
        a string
        """
        in_1 = Base("String")
        self.assertEqual(in_1.id, "String")
    def test_dict_base(self):
        """
        test_dict_base - change the id
        for dict
        """
        in_1 = Base({id: 1})
        self.assertEqual(in_1.id, {id: 1})
    
    def test_float_base(self):
        """
        test_float_base - change the id
        for float nul
        """
        in_1 = Base(float('NaN'))
        self.assertNotEqual(in_1.id, in_1.id)
    
    def test_list(self):
        """
        test_list - change the id
        for list
        """
        in_1 = Base([420])
        self.assertEqual(in_1.id, [420])
    def test_float2(self):
        """
        test_float2 - change id to
        float number
        """
        in_1 = Base(3.14)
        self.assertEqual(in_1.id, 3.14)
        
    def test_tuple(self):
        """
        test_tuple - change the id for a tuple
        """
        in_1 = Base((6, 9))
        self.assertEqual(in_1.id, (6, 9))
    
    def test_array(self):
        """
        test_array - change the id to
        array
        """
        in_1 = Base({4, 2, 0})
        self.assertEqual(in_1.id, {0, 2, 4})
if __name__ == '__main__':
    unittest.main()