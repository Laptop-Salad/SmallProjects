from fizz_buzz import fizz_buzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(fizz_buzz([1,2,3]), ["1","2","Fizz"], "Should be 1 2 Fizz")
    
    def test_non_list(self):
        with self.assertRaises(Exception):
            fizz_buzz(0)
    
    def test_non_integer(self):
        with self.assertRaises(Exception):
            fizz_buzz([1,2,"i"])


if __name__ == "__main__":
    unittest.main()