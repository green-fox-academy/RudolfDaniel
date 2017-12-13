import unittest
from rudolf_daniel_work import *

class TestStringMethods(unittest.TestCase):

    def test_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")


if __name__ == '__main__':
    unittest.main()