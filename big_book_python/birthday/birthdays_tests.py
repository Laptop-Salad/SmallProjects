from birthdays import *
import datetime
import unittest

class TestBirthdays(unittest.TestCase):
    def test_check_chance(self):
        self.assertEqual(calculate_chance(50955), 50.95)
        self.assertEqual(calculate_chance(0), 0)
        self.assertEqual(calculate_chance(100_000), 100)
    
    def test_check_matching_birth(self):
        matches = check_matching_birth([
            datetime.datetime(2023, 1, 30),
            datetime.datetime(2023, 2, 28),
            datetime.datetime(2023, 1, 30)])
                                       
        self.assertEqual(matches[0], 1)
        
        matches = check_matching_birth([
            datetime.datetime(2023, 1, 30),
            datetime.datetime(2023, 2, 28),
            datetime.datetime(2023, 3, 30)])
                                       
        self.assertEqual(matches[0], 0)
    
    def test_generate_birthdays(self):
        birthdays = generate_birthdays(2)
        self.assertEqual(len(birthdays), 2)
        
        birthdays = generate_birthdays(58)
        self.assertEqual(len(birthdays), 58)
        
        birthdays = generate_birthdays(100)
        self.assertEqual(len(birthdays), 100)
