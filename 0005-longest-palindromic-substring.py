import unittest


class TestLongestPalindrome(unittest.TestCase):

    def test_1(self):
        self.input = "babad"
        self.acceptable_outputs = ["bab", "aba"]
        self.run_test()

    def test_2(self):
        self.input = "cbbd"
        self.acceptable_outputs = ["bb"]
        self.run_test()

    def test_3(self):
        self.input = "a"
        self.acceptable_outputs = ["a"]
        self.run_test()

    def test_4(self):
        self.input = "abcd"
        self.acceptable_outputs = ["a", "b", "c", "d"]
        self.run_test()

    def test_5(self):
        self.input = "bb"
        self.acceptable_outputs = ["bb"]
        self.run_test()

    def test_is_palindrome(self):
        self.assertTrue(Solution().is_palindrome("aba"))
        self.assertTrue(Solution().is_palindrome("abba"))

    def run_test(self):
        self.assertIn(
            Solution().longestPalindrome(self.input),
            self.acceptable_outputs
        )


class Solution:
    def longestPalindrome(self, s: str) -> str:
        for l in range(len(s), 0, -1):
            for i in range(len(s) - l + 1):
                substring = s[i:i + l]
                if self.is_palindrome(substring):
                    return substring

    def is_palindrome(self, s: str) -> bool:
        for i in range(len(s) // 2 + 1):
            if s[i] != s[-(i+1)]:
                return False
        return True


if __name__ == '__main__':
    unittest.main()
