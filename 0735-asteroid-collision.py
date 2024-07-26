from typing import List
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.asteroids = [5, 10, -5]
        self.expected_output = [5, 10]
        self.run_test()

    def test_2(self):
        self.asteroids = [8, -8]
        self.expected_output = []
        self.run_test()

    def test_3(self):
        self.asteroids = [10, 2, -5]
        self.expected_output = [10]
        self.run_test()

    def test_4(self):
        self.asteroids = [-10, 2, -5]
        self.expected_output = [-10, -5]
        self.run_test()

    def test_5(self):
        self.asteroids = [8, 8, -8]
        self.expected_output = [8]
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().asteroidCollision(self.asteroids),
            self.expected_output
        )


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining_asteroids = []
        for asteroid in asteroids:
            while remaining_asteroids and asteroid < 0 < remaining_asteroids[-1]:
                if abs(asteroid) > remaining_asteroids[-1]:
                    remaining_asteroids.pop()
                    continue
                elif abs(asteroid) == remaining_asteroids[-1]:
                    remaining_asteroids.pop()
                break
            else:
                remaining_asteroids.append(asteroid)
        return remaining_asteroids


unittest.main()
