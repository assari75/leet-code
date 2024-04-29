import unittest


class TestReverse(unittest.TestCase):

    def test_1(self):
        self.input = 123
        self.expected_outputs = 321
        self.run_test()

    def test_2(self):
        self.input = -123
        self.expected_outputs = -321
        self.run_test()

    def test_3(self):
        self.input = 120
        self.expected_outputs = 21
        self.run_test()

    def test_4(self):
        self.input = -120
        self.expected_outputs = -21
        self.run_test()
        
    def test_5(self):
        self.input = 1534236469
        self.expected_outputs = 0
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().reverse(self.input),
            self.expected_outputs
        )


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = 0
        x = abs(x)
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10
            if result.bit_length() > 31:
                return 0
        return sign * result


unittest.main()
