import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.s = "leet**cod*e"
        self.expected_output = "lecoe"
        self.run_test()

    def test_2(self):
        self.s = "erase*****"
        self.expected_output = ""
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().removeStars(self.s),
            self.expected_output
        )


class Solution:
    def removeStars(self, s: str) -> str:
        non_stars_stack = []
        for c in s:
            if c == "*":
                non_stars_stack.pop()
            else:
                non_stars_stack.append(c)
        return "".join(non_stars_stack)


unittest.main()
