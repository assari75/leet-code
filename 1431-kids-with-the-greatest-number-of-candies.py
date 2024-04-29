from typing import List
import unittest


class TestKidsWithCandies(unittest.TestCase):

    def test_1(self):
        self.candies = [2, 3, 5, 1, 3]
        self.extra_candies = 3
        self.expected_output = [True, True, True, False, True]
        self.run_test()

    def test_2(self):
        self.candies = [4,2,1,1,2]
        self.extra_candies = 1
        self.expected_output = [True, False, False, False, False]
        self.run_test()

    def test_3(self):
        self.candies = [12, 1, 12]
        self.extra_candies = 10
        self.expected_output = [True, False, True]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().kidsWithCandies(self.candies, self.extra_candies),
            self.expected_output
        )


class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        max_candies = max(candies)
        return [count + extra_candies >= max_candies for count in candies]


unittest.main()
