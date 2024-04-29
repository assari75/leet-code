import unittest
from typing import List


class TestFindMedianSortedArrays(unittest.TestCase):

    def test_1(self):
        self.nums1 = [1, 3]
        self.nums2 = [2]
        self.expected_output = 2
        self.run_test()

    def test_2(self):
        self.nums1 = [1, 2]
        self.nums2 = [3, 4]
        self.expected_output = 2.5
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().findMedianSortedArrays(self.nums1, self.nums2),
            self.expected_output
        )


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0
        merged_list = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                merged_list.append(nums1[index1])
                index1 += 1
            else:
                merged_list.append(nums2[index2])
                index2 += 1
        
        if index1 < len(nums1):
            merged_list += nums1[index1:]
        
        if index2 < len(nums2):
            merged_list += nums2[index2:]

        return self.get_median_of_sorted_list(merged_list)
    
    def get_median_of_sorted_list(self, l: List[int]) -> float:
        if len(l) % 2 == 1:
            return l[len(l) // 2]
        return 0.5*(l[len(l) // 2 - 1] + l[len(l) // 2])


if __name__ == '__main__':
    unittest.main()
