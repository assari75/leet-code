import unittest


class TestMyAtoi(unittest.TestCase):

    def test_1(self):
        self.input = "42"
        self.expected_outputs = 42
        self.run_test()

    def test_2(self):
        self.input = "   -42"
        self.expected_outputs = -42
        self.run_test()

    def test_3(self):
        self.input = "4193 with words"
        self.expected_outputs = 4193
        self.run_test()

    def test_4(self):
        self.input = "-91283472332"
        self.expected_outputs = - 2 ** 31
        self.run_test()

    def test_5(self):
        self.input = ""
        self.expected_outputs = 0
        self.run_test()

    def test_6(self):
        self.input = "+"
        self.expected_outputs = 0
        self.run_test()

    def test_7(self):
        self.input = " "
        self.expected_outputs = 0
        self.run_test()

    def test_8(self):
        self.input = "words and 987"
        self.expected_outputs = 0
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().myAtoi(self.input),
            self.expected_outputs
        )


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s, sign = self.get_sign(s)
        if sign == 0:
            return 0
        num = self.get_num(s, sign)
        return num * sign

    def get_sign(self, s: str) -> tuple:
        if len(s) == 0:
            return s, 0
        if s[0].isdigit():
            return s, 1
        if s[0] == '+':
            return s[1:], 1
        if s[0] == '-':
            return s[1:], -1
        return s, 0

    def get_num(self, s: str, sign: int) -> int:
        num = 0
        for char in s:
            if not char.isdigit():
                return num
            num = num * 10 + int(char)
            if num.bit_length() >= 32:
                if sign == 1:
                    return 2 ** 31 - 1
                return 2 ** 31
        return num


unittest.main()
