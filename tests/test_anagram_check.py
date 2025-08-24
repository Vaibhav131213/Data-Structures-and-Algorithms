import unittest
from Python.Strings.anagram_check import isAnagram

class TestAnagramCheck(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(isAnagram("anagram", "nagaram"))
        self.assertFalse(isAnagram("rat", "car"))

if __name__ == "__main__":
    unittest.main()
