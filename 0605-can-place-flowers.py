from typing import List, Tuple
import unittest


class TestCanPlaceFlowers(unittest.TestCase):

    def test_1(self):
        self.flowerbed = [1, 0, 0, 0, 1]
        self.n = 1
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.flowerbed = [1, 0, 0, 0, 1]
        self.n = 2
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.flowerbed = [1, 0, 0, 1, 0]
        self.n = 1
        self.expected_output = False
        self.run_test()

    def test_4(self):
        self.flowerbed = [0, 0, 1, 0, 1]
        self.n = 1
        self.expected_output = True
        self.run_test()

    def test_5(self):
        self.flowerbed = [0]
        self.n = 1
        self.expected_output = True
        self.run_test()

    def test_6(self):
        self.flowerbed = [1]
        self.n = 1
        self.expected_output = False
        self.run_test()

    def test_7(self):
        self.flowerbed = [0, 0, 1, 0, 0]
        self.n = 1
        self.expected_output = True
        self.run_test()

    def test_8(self):
        self.flowerbed = [1, 0, 0, 0, 0, 1]
        self.n = 2
        self.expected_output = False
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().canPlaceFlowers(self.flowerbed, self.n),
            self.expected_output
        )


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        index = 0
        while n > 0 and index < l:
            if flowerbed[index] == 0 and (index == 0 or flowerbed[index-1] == 0) and (index == l-1 or flowerbed[index+1] == 0):
                index += 2
                n -= 1
            else:
                index += 1
        return n == 0


unittest.main()
