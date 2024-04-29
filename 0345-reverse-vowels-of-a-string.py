import unittest


class TestReverseVowels(unittest.TestCase):

    def test_1(self):
        self.input = "hello"
        self.expected_output = "holle"
        self.run_test()

    def test_2(self):
        self.input = "leetcode"
        self.expected_output = "leotcede"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().reverseVowels(self.input),
            self.expected_output
        )


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left_index = 0
        right_index = len(s) - 1
        left_vowel_found = False
        right_vowel_found = False
        while left_index < right_index:
            if self.is_vowel(s[left_index]):
                left_vowel_found = True
            else:
                left_index += 1
            if self.is_vowel(s[right_index]):
                right_vowel_found = True
            else:
                right_index -= 1
            if left_vowel_found and right_vowel_found:
                s[left_index], s[right_index] = s[right_index], s[left_index]
                left_vowel_found, right_vowel_found = False, False
                left_index += 1
                right_index -= 1
        return "".join(s)


    def is_vowel(self, char: str) -> bool:
        return char in "aeiouAEIOU"


unittest.main()
