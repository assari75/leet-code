from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.arr = [1, 2, 2, 1, 1, 3]
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.arr = [1, 2]
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        self.expected_output = True
        self.run_test()

    def test_4(self):
        self.arr = [3, 5, -2, -3, -6, -6]
        self.expected_output = False
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().uniqueOccurrences(self.arr),
            self.expected_output
        )


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        occurances = []
        i = 0
        while i < len(arr):
            count = 1
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                count += 1
                i += 1
            occurances.append(count)
            i += 1

        occurances.sort()
        for i in range(1, len(occurances)):
            if occurances[i] == occurances[i - 1]:
                return False
        return True



unittest.main()
