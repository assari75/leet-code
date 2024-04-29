import unittest


class TestMergeAlternately(unittest.TestCase):

    def test_1(self):
        self.word1 = "abc"
        self.word2 = "pqr"
        self.expected_output = "apbqcr"
        self.run_test()

    def test_2(self):
        self.word1 = "ab"
        self.word2 = "pqrs"
        self.expected_output = "apbqrs"
        self.run_test()

    def test_3(self):
        self.word1 = "abcd"
        self.word2 = "pq"
        self.expected_output = "apbqcd"
        self.run_test()

    def test_4(self):
        self.word1 = "abc"
        self.word2 = ""
        self.expected_output = "abc"
        self.run_test()

    def test_5(self):
        self.word1 = ""
        self.word2 = "pqr"
        self.expected_output = "pqr"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().mergeAlternately(self.word1, self.word2),
            self.expected_output
        )


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_index = 0
        word2_index = 0
        word1_len = len(word1)
        word2_len = len(word2)
        result = ""
        while word1_index < word1_len and word2_index < word2_len:
            result = result + word1[word1_index] + word2[word2_index]
            word1_index += 1
            word2_index += 1
        return result + word1[word1_index:] + word2[word2_index:]

unittest.main()
