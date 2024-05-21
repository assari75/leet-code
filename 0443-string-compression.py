from typing import List
import unittest


class TestReverseWords(unittest.TestCase):

    def test_1(self):
        self.input = ["a","a","b","b","c","c","c"]
        self.expected_output = 6
        self.modified_input = ["a","2","b","2","c","3"]
        self.run_test()

    def test_2(self):
        self.input = ["a"]
        self.expected_output = 1
        self.modified_input = ["a"]
        self.run_test()

    def test_3(self):
        self.input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.expected_output = 4
        self.modified_input = ["a","b","1","2"]
        self.run_test()
    
    def test_4(self):
        self.input = ["a","b","b","a","a","b","c"]
        self.expected_output = 7
        self.modified_input = ["a","b","2","a","2","b","c"]
        self.run_test()

    def run_test(self):
        output = Solution().compress(self.input)
        self.assertEqual(self.input, self.modified_input)
        self.assertEqual(output, self.expected_output)


class Solution:
    def compress(self, chars: List[str]) -> int:
        num = 1
        index = 1
        last_char = chars[0]
        while index < len(chars):
            if chars[index] == last_char:
                num += 1
                chars.pop(index)
            else:
                last_char = chars[index]
                if num > 1:
                    self.insert_num_digits(chars, num, index)
                    index += len(str(num))
                    num = 1
                index += 1
                    
        if num > 1:
            self.insert_num_digits(chars, num, index)
        return len(chars)

    def insert_num_digits(self, chars: List[str], num: int, index: int):
        i = index
        for digit in str(num):
            chars.insert(i, digit)
            i += 1

unittest.main()
