from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.input = [0,1,0,3,12]
        self.expected_output = [1,3,12,0,0]
        self.run_test()

    def test_2(self):
        self.input = [0]
        self.expected_output = [0]
        self.run_test()

    def test_3(self):
        self.input = [2, 1]
        self.expected_output = [2, 1]
        self.run_test()

    def test_4(self):
        self.input = [0, 0, 1]
        self.expected_output = [1, 0, 0]
        self.run_test()

    def run_test(self):
        Solution().moveZeroes(self.input)
        self.assertEqual(self.input, self.expected_output)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


unittest.main()
