from bagels import check_guess, check_keywords
import unittest

class TestBagels(unittest.TestCase):
    def test_check_guess(self):
        self.assertEqual(check_guess("123", "100"), "Fermi 1| Pico 0| Wrong 2|")
        self.assertEqual(check_guess("100", "100"), "You got it!")
        self.assertEqual(check_guess("23", "43"), "Fermi 1| Pico 0| Wrong 1|")
        self.assertEqual(check_guess("127", "000"), "Bagels")
    
    def test_check_keywords(self):
        self.assertEqual(check_keywords("hint", "333", ["3", "3", "3"], 0), ["hint", ["3", "3"]])
        self.assertEqual(check_keywords("hint", "333", [], 0), ["hints-none"])
        self.assertEqual(check_keywords("force", "333", ["3", "3", "3"], 0), ["force"])
        self.assertEqual(check_keywords("123", "333", ["3", "3", "3"], 0), [""])
        
        
if __name__ == "__main__":
    unittest.main()