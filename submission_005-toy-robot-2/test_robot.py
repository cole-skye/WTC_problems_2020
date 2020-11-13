import unittest
from unittest.mock import patch
import robot
import sys 
from io import StringIO 

class test_robot(unittest.TestCase):


    @patch("sys.stdin", StringIO("Hal\nforward 10\noff\n"))
    def test_forward(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("Hal\nback 10\noff\n"))
    def test_back(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""",output)


    @patch("sys.stdin", StringIO("Hal\nright\noff\n"))
    def test_right(self):
        with patch("sys.stdout",StringIO()) as out:
            robot.robot_start()
        
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""",output)


    @patch("sys.stdin", StringIO("Hal\nleft\noff\n"))
    def test_left(self):
        with patch("sys.stdout",StringIO()) as out:
            robot.robot_start()
        
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""",output)
        
if __name__ == '__main__':
    unittest.main()