# test_string_operations.py
import unittest
from string_operations import reverse_string, count_words, is_palindrome

class TestStringOperations(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_count_words(self):
        self.assertEqual(count_words("Hello, World!"), 2)
        self.assertEqual(count_words("This is a test"), 4)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("kayak"))
        self.assertFalse(is_palindrome("Able was I, ere I saw Elba"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Jenkins"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()