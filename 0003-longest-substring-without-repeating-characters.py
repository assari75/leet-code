import unittest


class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_1(self):
        self.input = "abcabcbb"
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.input = "bbbbb"
        self.expected_output = 1
        self.run_test()

    def test_3(self):    
        self.input = "pwwkew"
        self.expected_output = 3
        self.run_test()

    def test_4(self):
        self.input = ""
        self.expected_output = 0
        self.run_test()

    def test_5(self):
        self.input = "a"
        self.expected_output = 1
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().lengthOfLongestSubstring(self.input),
            self.expected_output
        )


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for index in range(len(s)):
            substring = []
            for char in s[index:]:
                if char not in substring:
                    substring.append(char)
                    result = len(substring) if len(substring) > result else result
                else:
                    break
        return result


if __name__ == '__main__':
    unittest.main()
