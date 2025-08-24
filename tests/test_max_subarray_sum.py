import unittest
from Python.Arrays.max_subarray_sum import maxSubArray

class TestMaxSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray([1]), 1)
        self.assertEqual(maxSubArray([5,4,-1,7,8]), 23)

if __name__ == "__main__":
    unittest.main()
    