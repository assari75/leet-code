from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.nums1 = [1, 2, 3]
        self.nums2 = [2, 4, 6]
        self.expected_output = [[1, 3], [4, 6]]
        self.run_test()

    def test_2(self):
        self.nums1 = [1, 2, 3, 3]
        self.nums2 = [1, 1, 2, 2]
        self.expected_output = [[3], []]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().findDifference(self.nums1, self.nums2),
            self.expected_output
        )


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = [[], []]
        for num in set1:
            if num not in set2:
                ans[0].append(num)
        for num in set2:
            if num not in set1:
                ans[1].append(num)
        return ans


unittest.main()
