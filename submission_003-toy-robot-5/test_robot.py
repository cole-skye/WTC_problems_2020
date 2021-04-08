import unittest
import io
import sys
import robot
from unittest.mock import patch
from io import StringIO
import maze.obstacles as obstacles


class TestToyRobot(unittest.TestCase):
    
    

    def test_add_command_history(self):
        """
        Tests if command history gets added correctly
        """      
        robot.history = []  
        commands = ['forward 10','right','back 10']
        
        for item in commands:
            robot.add_to_history(item)
        self.assertEqual(robot.history,['forward 10','right','back 10'])
        robot.history = []


    @patch('sys.stdin', StringIO("HAL\nForward 10\nright\nback 10\noff"))
    def test_robot(self):
        """
        Test robot output
        """        
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,10).
HAL: What must I do next? HAL: Shutting down..\n''')


    @patch('sys.stdin', StringIO("Jeff\nForward 10\nleft\nback 10\noff"))
    def test_robot_1(self):
        """
        Test robot output
        """        
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? Jeff: Hello kiddo!
Jeff: Loaded obstacles.
Jeff: What must I do next?  > Jeff moved forward by 10 steps.
 > Jeff now at position (0,10).
Jeff: What must I do next?  > Jeff turned left.
 > Jeff now at position (0,10).
Jeff: What must I do next?  > Jeff moved back by 10 steps.
 > Jeff now at position (10,10).
Jeff: What must I do next? Jeff: Shutting down..\n''')

if __name__ == "__main__":
    unittest.main()