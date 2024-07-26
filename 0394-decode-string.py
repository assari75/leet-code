import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.s = "3[a]2[bc]"
        self.expected_output = "aaabcbc"
        self.run_test()

    def test_2(self):
        self.s = "3[a2[c]]"
        self.expected_output = "accaccacc"
        self.run_test()

    def test_3(self):
        self.s = "2[abc]3[cd]ef"
        self.expected_output = "abcabccdcdcdef"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().decodeString(self.s),
            self.expected_output
        )


class Solution:
    def decodeString(self, s: str) -> str:
        open_bracket_indexes = []
        number_indexes = []
        index = 0
        while index < len(s):
            c = s[index]
            if c.isdigit():
                number_indexes.append(index)
                while s[index].isdigit():
                    index += 1
                else:
                    continue
            elif c == "[":
                open_bracket_indexes.append(index)
                index += 1
            elif c == "]":
                last_open_bracket_index = open_bracket_indexes.pop()
                last_number_index = number_indexes.pop()
                num = int(s[last_number_index:last_open_bracket_index])
                string = num * s[last_open_bracket_index+1:index]
                s = s[:last_number_index] + string + s[index+1:]
                index = last_number_index + len(string)
            else:
                index += 1
        return s
            

unittest.main()
