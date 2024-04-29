import unittest
from typing import List


class TestAddTwoNumbers(unittest.TestCase):

    def test_1(self):
        self.l1 = [2, 4, 3]
        self.l2 = [5, 6, 4]
        self.expected_output = [7, 0, 8]
        self.run_test()

    def test_2(self):
        self.l1 = [0]
        self.l2 = [0]
        self.expected_output = [0]
        self.run_test()

    def test_3(self):
        self.l1 = [9, 9, 9, 9, 9, 9, 9]
        self.l2 = [9, 9, 9, 9]
        self.expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().addTwoNumbers(self.l1, self.l2),
            self.expected_output
        )


class Solution:
    def addTwoNumbers(self, l1: List[int], l2: List[int]) -> List[int]:
        n1 = self.convert_list_to_number(l1)
        n2 = self.convert_list_to_number(l2)
        return self.convert_number_to_list(n1 + n2)

    def convert_list_to_number(self, l: List[int]) -> int:
        result = 0
        power = 1
        for num in l:
            result += power*num
            power *= 10
        return result

    def convert_number_to_list(self, n: int) -> List[int]:
        return reversed([int(x) for x in str(n)])


if __name__ == '__main__':
    unittest.main()
