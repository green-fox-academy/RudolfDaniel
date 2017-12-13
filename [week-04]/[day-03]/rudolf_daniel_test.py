import unittest
from rudolf_daniel_work import *

class TestStringMethods(unittest.TestCase):

    def test_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")

    def test_summa(self):
        list_of_numbers = Sum()
        self.assertEqual(list_of_numbers.summa([]), 0)
    def test_summa(self):
        list_of_numbers = Sum()
        self.assertEqual(list_of_numbers.summa([5]), 5)
    def test_summa(self):
        list_of_numbers = Sum()
        self.assertEqual(list_of_numbers.summa([11, 22, 33]), 66)
    def test_summa(self):
        list_of_numbers = Sum()
        self.assertEqual(list_of_numbers.summa([0]), 0)

    def test_anagram(self):
        anagram = Anagram()
        self.assertEqual(anagram.is_anagram("nana", "anna"), True or False)

    def test_countletters(self):
        dictionary = CountLetters()
        self.assertEqual(dictionary.dictionary_maker("letter"), {"l":1, "e":2, "t":2, "r":1})

if __name__ == '__main__':
    unittest.main()