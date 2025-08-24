import unittest
from Python.Strings.longest_substring import lengthOfLongestSubstring

class TestLongestSubstring(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == "__main__":
    unittest.main()
