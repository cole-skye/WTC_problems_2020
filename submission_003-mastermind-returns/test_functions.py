import unittest
from unittest.mock import patch
from io import StringIO
from mastermind import *
import sys

class Test_functions(unittest.TestCase):

    """
        Checking to see whether the code is between 1 and 8, also 
        checking to see whether its a 4 digit code
    """

    def test_create_code(self):
        for i in range (100):
            code = create_code()

            self.assertNotIn(0, code)
            self.assertNotIn(9, code)
            self.assertEqual(len(code), 4)   
            # print(code)         

    """     
        Checking to see if the code is true or false
    """
    def test_correctness(self):

        sys.stdout = StringIO()
        self.assertTrue(check_correctness(4 , (4, 0)))
        self.assertEqual(sys.stdout.getvalue(), 'Congratulations! You are a codebreaker!\n')

        sys.stdout = StringIO()
        self.assertFalse(check_correctness(3, (3, 0)))
        self.assertEqual(sys.stdout.getvalue(), 'Turns left: 9\n')

    """
        Checking the answer input is only 4 characters
    """
    @patch("sys.stdin", StringIO("1234\n"))
    def test_get_answer_input(self):
            self.assertEqual(get_answer_input(), "1234")

    """
        checking the take turn output

    """
    @patch("sys.stdin", StringIO("1234\n1234\n5678\n"))
    def test_take_turn(self):

        sys.stdout = StringIO()
        self.assertEqual(take_turn([1,2,3,4]), (4, 0))
        self.assertEqual(take_turn([1,3,2,4]), (2, 2))
        self.assertEqual(take_turn([1,2,3,4]), (0, 0))



if __name__ == '__main__':
    unittest.main() 