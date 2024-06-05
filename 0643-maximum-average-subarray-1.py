from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums = [1, 12, -5, -6, 50, 3]
        self.k = 4
        self.expected_output = 12.75
        self.run_test()

    def test_2(self):
        self.nums = [5]
        self.k = 1
        self.expected_output = 5
        self.run_test()

    def test_3(self):
        self.nums = [0, 1, 1, 3, 3]
        self.k = 4
        self.expected_output = 2
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().findMaxAverage(self.nums, self.k),
            self.expected_output
        )


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        return max_sum/k

unittest.main()
