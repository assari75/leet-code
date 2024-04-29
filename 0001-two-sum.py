import unittest
from typing import List


class TestTwoSum(unittest.TestCase):

    def test_1(self):
        self.nums = [2, 7, 11, 15]
        self.target = 9
        self.expected_output = [0, 1]
        self.run_test()

    def test_2(self):
        self.nums = [3, 2, 4]
        self.target = 6
        self.expected_output = [1, 2]
        self.run_test()

    def test_3(self):    
        self.nums = [3, 3]
        self.target = 6
        self.expected_output = [0, 1]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().twoSum(self.nums, self.target),
            self.expected_output
        )


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            if num in dict:
                return [dict[num], index]
            else:
                dict[target-num]=index


if __name__ == '__main__':
    unittest.main()
