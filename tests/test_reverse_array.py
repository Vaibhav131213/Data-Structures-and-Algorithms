import unittest
from Python.Arrays.reverse_array import reverseArray

class TestReverseArray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(reverseArray([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverseArray([10]), [10])
        self.assertEqual(reverseArray([]), [])

if __name__ == "__main__":
    unittest.main()
