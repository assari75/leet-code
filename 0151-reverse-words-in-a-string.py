import unittest


class TestReverseWords(unittest.TestCase):

    def test_1(self):
        self.input = "the sky is blue"
        self.expected_output = "blue is sky the"
        self.run_test()

    def test_2(self):
        self.input = "  hello world  "
        self.expected_output = "world hello"
        self.run_test()

    def test_3(self):
        self.input = "a good   example"
        self.expected_output = "example good a"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().reverseWords(self.input),
            self.expected_output
        )


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


unittest.main()
