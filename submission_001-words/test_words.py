import unittest
import word_processor

class Testword_processor(unittest.TestCase):

    def test_word_list(self):
        self.assertEqual(['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you'], word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?'))

    def test_longer_than(self):
        self.assertEqual(['interesting','understatement'], word_processor.words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?'))
    
    def test_lengths_map(self):
        self.assertEqual({2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}, word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?'))

    def test_letters_count_map(self):
        self.assertEqual({'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
,word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?'))

    def test_most_used_character(self):
        self.assertEqual(None , word_processor.most_used_character(''))
        self.assertEqual('e' , word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?'))


if __name__ == '__main__':
    unittest.main()
