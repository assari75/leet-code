from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.input = [1, 2, 3, 4, 5]
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.input = [5, 4, 3, 2, 1]
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.input = [2, 1, 5, 0, 4, 6]
        self.expected_output = True
        self.run_test()

    def test_4(self):
        self.input = [2, 1, 4, 0, 6, 1]
        self.expected_output = True
        self.run_test()

    def test_5(self):
        self.input = [0, 4, 2, 1, 0, -1, -3]
        self.expected_output = False
        self.run_test()

    def test_6(self):
        self.input = [20, 100, 10, 12, 5, 13]
        self.expected_output = True
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().increasingTriplet(self.input),
            self.expected_output
        )


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        MAX = 2 ** 31 - 1
        a, b = MAX, MAX
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False


unittest.main()
