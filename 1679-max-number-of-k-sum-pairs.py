from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums = [1, 2, 3, 4]
        self.k = 5
        self.expected_output = 2
        self.run_test()

    def test_2(self):
        self.nums = [3, 1, 3, 4, 3]
        self.k = 6
        self.expected_output = 1
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().maxOperations(self.nums, self.k),
            self.expected_output
        )


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operations = 0
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            sum = nums[left_pointer] + nums[right_pointer]
            if sum == k:
                operations += 1
                left_pointer += 1
                right_pointer -= 1
            elif sum < k:
                left_pointer += 1
            elif sum > k:
                right_pointer -= 1
        return operations

unittest.main()
