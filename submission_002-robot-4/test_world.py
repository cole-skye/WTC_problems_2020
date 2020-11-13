import unittest
from world.text import world as txt
import sys 
from io import StringIO


class test_TextWorld(unittest.TestCase):


    def test_update_1(self):

        txt.position_x = 50
        txt.position_y = 50
        txt.current_direction_index = 2
        self.assertTrue(txt.update_position(50))


    def test_update_2(self):

        txt.position_x = 50
        txt.position_y = 150
        txt.current_direction_index = 1
        self.assertFalse(txt.update_position(60))



    def test_update_3(self):

        txt.position_x = 50
        txt.position_y = 0
        txt.current_direction_index = 3
        self.assertTrue(txt.update_position(60))


    def test_update_4(self):
        
        txt.position_x = 50
        txt.position_y = 180
        txt.current_direction_index = 0
        self.assertFalse(txt.update_position(60))


if __name__ == "__main__":
    unittest.main()