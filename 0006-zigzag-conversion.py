import unittest


class TestConvert(unittest.TestCase):

    def test_1(self):
        self.input = "PAYPALISHIRING"
        self.rows = 3
        self.expected_outputs = "PAHNAPLSIIGYIR"
        self.run_test()

    def test_2(self):
        self.input = "PAYPALISHIRING"
        self.rows = 4
        self.expected_outputs = "PINALSIGYAHRPI"
        self.run_test()

    def test_3(self):
        self.input = "AB"
        self.rows = 1
        self.expected_outputs = "AB"
        self.run_test()

    def test_4(self):
        self.input = "ABC"
        self.rows = 1
        self.expected_outputs = "ABC"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().convert(self.input, self.rows),
            self.expected_outputs
        )


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        index = 1
        direction = False # True for increasing and False for decreasing
        direction_dict = {
            True: 1,
            False: -1
        }
        for ch in s:
            result[index - 1] += ch
            if index == 1 or index == numRows:
                direction = not direction
            index += direction_dict[direction]
        return "".join(result)


if __name__ == '__main__':
    unittest.main()
