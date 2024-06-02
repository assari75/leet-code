from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.input = [1,8,6,2,5,4,8,3,7]
        self.expected_output = 49
        self.run_test()

    def test_2(self):
        self.input = [1, 1]
        self.expected_output = 1
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().maxArea(self.input),
            self.expected_output
        )


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        left_height = height[left_index]
        right_height = height[right_index]
        h = min(left_height, right_height)
        max_area = (right_index - left_index) * h
        while left_index < right_index:
            found = False
            if left_height == h:
                left_index += 1
                if height[left_index] > left_height:
                    left_height = height[left_index]
                    found = True
            elif right_height == h:
                right_index -= 1
                if height[right_index] > right_height:
                    right_height = height[right_index]
                    found = True
            if found:
                h = min(left_height, right_height)
                max_area = max(max_area, (right_index - left_index) * h)
        return max_area


unittest.main()
