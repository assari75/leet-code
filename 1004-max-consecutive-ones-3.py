from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        self.k = 2
        self.expected_output = 6
        self.run_test()

    def test_2(self):
        self.nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        self.k = 3
        self.expected_output = 10
        self.run_test()

    def test_3(self):
        self.nums = [0,0,0,1]
        self.k = 4
        self.expected_output = 4
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().longestOnes(self.nums, self.k),
            self.expected_output
        )


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left_pointer = 0
        right_pointer = 0
        longest_ones = 0
        while right_pointer < len(nums):
            if nums[right_pointer] == 1:
                right_pointer += 1
            elif zeros < k:
                right_pointer += 1
                zeros += 1
            else:
                if nums[left_pointer] == 0:
                    zeros -= 1
                left_pointer += 1
            longest_ones = max(longest_ones, right_pointer-left_pointer)

        return longest_ones


unittest.main()
