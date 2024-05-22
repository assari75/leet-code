import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.s = "abc"
        self.t = "ahbgdc"
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.s = "axc"
        self.t = "ahbgdc"
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.s = ""
        self.t = "ahbgdc"
        self.expected_output = True
        self.run_test()

    def test_4(self):
        self.s = "b"
        self.t = "abc"
        self.expected_output = True
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().isSubsequence(self.s, self.t),
            self.expected_output
        )


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0
        while t_pointer < len(t) and s_pointer < len(s):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)


unittest.main()
