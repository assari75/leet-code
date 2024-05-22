import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.input = 121
        self.expected_outputs = True
        self.run_test()

    def test_2(self):
        self.input = -121
        self.expected_outputs = False
        self.run_test()

    def test_3(self):
        self.input = 10
        self.expected_outputs = False
        self.run_test()

    def test_4(self):
        self.input = 1
        self.expected_outputs = True
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().isPalindrome(self.input),
            self.expected_outputs
        )


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp = temp // 10
        return reversed_num == x


unittest.main()
