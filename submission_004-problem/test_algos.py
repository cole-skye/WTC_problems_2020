import unittest
from unittest.mock import patch
from io import StringIO
import super_algos 
import sys

class test_algos(unittest.TestCase):

    def test_find_min(self):

        self.assertEqual(-1, super_algos.find_min([]))
        self.assertEqual(-1, super_algos.find_min([1,2,'a',4,5]))
        self.assertEqual(2, super_algos.find_min([2]))
        self.assertEqual(1, super_algos.find_min([1,2,3,4,5]))

    def test_sum_all(self):

        self.assertEqual(-1, super_algos.sum_all([]))
        self.assertEqual(-1, super_algos.sum_all([1,2,'a',4,5]))
        self.assertEqual(2, super_algos.sum_all([2]))
        self.assertEqual(15, super_algos.sum_all([1,2,3,4,5]))
    
    def test_find_possible_strings(self):

        self.assertEqual([], super_algos.find_possible_strings([],3))
        self.assertEqual([], super_algos.find_possible_strings(['a',1,'c'],3))
        self.assertEqual(['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 
        'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 
        'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc'], super_algos.find_possible_strings(['a','b','c'],3))

if __name__ == '__main__':
    unittest.main()