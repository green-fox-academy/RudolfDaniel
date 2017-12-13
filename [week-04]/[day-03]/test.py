import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(extend.add(21, 1), 22)

    def test_add_second(self):
        self.assertEqual(extend.add(5, 1), 6)

    def test_max_of_three(self):
        self.assertEqual(extend.max_of_three(5, 410, 3), 410)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(1, 4, 5), 5)

    def test_median(self):
        self.assertEqual(extend.median([9,3,5]),5)

    def test_median_second(self):
        self.assertEqual(extend.median([10, 2, 5, 6, 99, 7, 1]), 6)

    def test_is_vovel(self):
        self.assertFalse(extend.is_vovel('z'))

    def test_is_vovel_second(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_translate(self):
        self.assertEqual(extend.translate('alma'), 'avalmava')

    def test_translate_second(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()