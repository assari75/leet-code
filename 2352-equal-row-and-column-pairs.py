from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.grid = [
            [3, 2, 1],
            [1, 7, 6],
            [2, 7, 7],
        ]
        self.expected_output = 1
        self.run_test()

    def test_2(self):
        self.grid = [
            [3, 1, 2, 2],
            [1, 4, 4, 5],
            [2, 4, 2, 2],
            [2, 4, 2, 2],
        ]
        self.expected_output = 3
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().equalPairs(self.grid),
            self.expected_output
        )


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_dict = {}
        for row in grid:
            rows_dict[tuple(row)] = rows_dict.get(tuple(row), 0) + 1
        pairs = 0
        for j in range(len(grid)):
            column = [grid[i][j] for i in range(len(grid[0]))]
            pairs += rows_dict.get(tuple(column), 0)
        return pairs


unittest.main()
