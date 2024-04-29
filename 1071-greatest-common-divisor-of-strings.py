from typing import Generator
import unittest


class TestGCDOfStrings(unittest.TestCase):

    def test_1(self):
        self.str1 = "ABCABC"
        self.str2 = "ABC"
        self.expected_output = "ABC"
        self.run_test()

    def test_2(self):
        self.str1 = "ABABAB"
        self.str2 = "ABAB"
        self.expected_output = "AB"
        self.run_test()

    def test_3(self):
        self.str1 = "LEET"
        self.str2 = "CODE"
        self.expected_output = ""
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().gcdOfStrings(self.str1, self.str2),
            self.expected_output
        )


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for length in self.generate_common_divisors(len(str1), len(str2)):
            div = str1[:length]
            if self.is_divisor_of_string(div, str1) and self.is_divisor_of_string(div, str2):
                return div
        return ""

    def generate_common_divisors(self, num1: int, num2: int) -> Generator[int, None, None]:
        for n in range(min(num1, num2), 1, -1):
            if (num1 % n == 0) and (num2 % n == 0):
                yield n
        yield 1

    def is_divisor_of_string(self, div: str, s: str) -> bool:
        temp_string = ""
        temp_l = 0
        div_l = len(div)
        l = len(s)
        while temp_l < l:
            temp_string += div
            temp_l += div_l
            if s[:temp_l] != temp_string:
                return False
        return True


unittest.main()
