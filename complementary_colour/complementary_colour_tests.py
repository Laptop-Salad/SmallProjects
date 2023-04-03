from complementary_colour import get_complementary_colour
import unittest

class TestComplementaryColour(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(get_complementary_colour(40, 174, 80), (215, 81, 175), "Should be 215 81 175")
    
    def test_below(self):
        with self.assertRaises(Exception):
            get_complementary_colour(267, 174, 80)
    
    def test_above(self):
        with self.assertRaises(Exception):
            get_complementary_colour(-6, 7, 10)

if __name__ == "__main__":
    unittest.main()