import unittest
from maze import obstacles as obs

class test_obstacles(unittest.TestCase):


    # def test_ob_blocked_1(self):

    #     obs.obstacles = [(60,40),(-100,5)]
        
    #     result = obs.is_path_blocked((0),(40),(70),(40))
    #     self.assertTrue(result)

    # def test_ob_blocked_3(self):

    #     obs.obstacles = [(40,90)]
        
    #     result = obs.is_position_blocked((40),(90))
    #     self.assertTrue(result)


    def test_ob_blocked_2(self):

        obs.obstacles = [(-60,180)]
        
        result = obs.is_path_blocked((0),(40),(-20),(40))
        self.assertFalse(result)


    def test_ob_blocked_4(self):

        obs.obstacles = [(60,40)]
        
        result = obs.is_position_blocked((40),(40))
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()