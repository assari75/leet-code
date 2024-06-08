from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums = [1, 1, 0, 1]
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        self.expected_output = 5
        self.run_test()

    def test_3(self):
        self.nums = [1, 1, 1]
        self.expected_output = 2
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().longestSubarray(self.nums),
            self.expected_output
        )


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left_pointer = 0
        longest_ones = 0
        for right_pointer, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > 1:
                if nums[left_pointer] == 0:
                    zeros -= 1
                left_pointer += 1
            longest_ones = max(longest_ones, right_pointer-left_pointer)
        return longest_ones


unittest.main()
