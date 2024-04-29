from typing import List
import unittest


class TestProductExceptSelf(unittest.TestCase):

    def test_1(self):
        self.input = [1, 2, 3, 4]
        self.expected_output = [24, 12, 8, 6]
        self.run_test()

    def test_2(self):
        self.input = [-1, 1, 0, -3, 3]
        self.expected_output = [0, 0, 9, 0, 0]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().productExceptSelf(self.input),
            self.expected_output
        )


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        return result


unittest.main()
