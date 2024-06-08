from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.gain = [-5, 1, 5, 0, -7]
        self.expected_output = 1
        self.run_test()

    def test_2(self):
        self.gain = [-4, -3, -2, -1, 4, 3, 2]
        self.expected_output = 0
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().largestAltitude(self.gain),
            self.expected_output
        )


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest_altitude = 0
        current_altitude = 0
        for num in gain:
            current_altitude += num
            if num > 0:
                largest_altitude = max(largest_altitude, current_altitude)
        return largest_altitude


unittest.main()
