from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums = [1, 7, 3, 6, 5, 6]
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.nums = [1, 2, 3]
        self.expected_output = -1
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().pivotIndex(self.nums),
            self.expected_output
        )


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for index, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return index
            left_sum += num
        return -1


unittest.main()
