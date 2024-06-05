import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.s = "abciiidef"
        self.k = 3
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.s = "aeiou"
        self.k = 2
        self.expected_output = 2
        self.run_test()

    def test_3(self):
        self.s = "leetcode"
        self.k = 3
        self.expected_output = 2
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().maxVowels(self.s, self.k),
            self.expected_output
        )


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = ("a", "e", "i", "o", "u")
        current_vowels = 0
        for ch in s[:k]:
            if ch in VOWELS:
                current_vowels += 1
        max_vowels = current_vowels
        for i in range(k, len(s)):
            if s[i] in VOWELS:
                current_vowels += 1
            if s[i-k] in VOWELS:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels


unittest.main()
