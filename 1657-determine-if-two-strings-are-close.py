import string
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.word1 = "abc"
        self.word2 = "bca"
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.word1 = "a"
        self.word2 = "aa"
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.word1 = "cabbba"
        self.word2 = "abbccc"
        self.expected_output = True
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().closeStrings(self.word1, self.word2),
            self.expected_output
        )


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        self.empty_occurances = {ch: 0 for ch in string.ascii_lowercase}
        word1_occurances = self.get_occurances(word1)
        word2_occurances = self.get_occurances(word2)
        for ch in string.ascii_lowercase:
            if bool(word1_occurances[ch]) != bool(word2_occurances[ch]):
                return False
        return sorted(word1_occurances.values()) == sorted(word2_occurances.values())

    def get_occurances(self, word: str) -> dict:
        occurances = self.empty_occurances.copy()
        for char in word:
            occurances[char] += 1
        return occurances


unittest.main()
