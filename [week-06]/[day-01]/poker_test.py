import unittest

class Poker(unittest.TestCase):

    def test_poker(self):
        self.assertEqual(("Black: 2H 3D 5S 9C KD", "White: 2C 3H 4S 8C AH"), "White wins! - (High card: Ace)")

if __name__ == '__main__':
    unittest.main()