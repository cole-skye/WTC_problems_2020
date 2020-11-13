import unittest
from unittest.mock import patch
import robot
import sys 
from io import StringIO

from robot import output 


class test_robot(unittest.TestCase):


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay\noff\n"))
    def test_do_replay(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (15,10).
 > HAL turned right.
 > HAL now at position (15,10).
 > HAL moved forward by 5 steps.
 > HAL now at position (15,5).
 > HAL replayed 3 commands.
 > HAL now at position (15,5).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nreplay 3-1\noff\n"))
    def test_do_replay_2(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,7).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,9).
 > HAL replayed 2 commands.
 > HAL now at position (0,9).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nreplay 2\noff\n"))
    def test_do_replay_3(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 3 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL replayed 3 commands silently.
 > HAL now at position (15,5).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nforward 10\nreplay silent 2\noff\n"))
    def test_replay_silent2(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (15,10).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (30,10).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nforward 10\nreplay silent 3-1\noff\n"))
    def test_replay_silent3(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (15,10).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (15,5).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (10,10).
 > HAL turned right.
 > HAL now at position (10,10).
 > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
 > HAL replayed 3 commands in reverse.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay reversed 2\noff\n"))
    def test_replay_reversed2(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (5,10).
 > HAL moved forward by 10 steps.
 > HAL now at position (5,0).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (5,0).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nleft\nreplay reversed 3-1\noff\n"))
    def test_replay_reversed3(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,15).
 > HAL turned right.
 > HAL now at position (5,15).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (5,15).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL replayed 3 commands in reverse silently.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nreplay reversed silent 2\noff\n"))
    def test_replay_reversed_silent2(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (5,0).
HAL: What must I do next? HAL: Shutting down..""" ,output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 5\nback 20\nreplay reversed silent 3-1\noff\n"))
    def test_replay_reversed_silent3(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (5,10).
HAL: What must I do next?  > HAL moved back by 20 steps.
 > HAL now at position (-15,10).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (-10,10).
HAL: What must I do next? HAL: Shutting down..""" ,output)

    @patch("sys.stdin", StringIO("HAL\nhelp\noff\n"))
    def test_help(self):
        with patch("sys.stdout", StringIO()) as out:
            robot.robot_start()
        
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays previous commands
REPLAY SILENT - replays previous commands silently
REPLAY REVERSED - replays previous commands in reverse
REPLAY REVERSED SILENT - replays previous commands silently in reverse

 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""",output)


if __name__ == '__main__':
    unittest.main()