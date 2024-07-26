from collections import deque
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.senate = "RD"
        self.expected_output = "Radiant"
        self.run_test()

    def test_2(self):
        self.senate = "RDD"
        self.expected_output = "Dire"
        self.run_test()

    def test_3(self):
        self.senate = "RDDR"
        self.expected_output = "Radiant"
        self.run_test()

    def test_4(self):
        self.senate = "RDDRD"
        self.expected_output = "Dire"
        self.run_test()

    def test_5(self):
        self.senate = "DDRRR"
        self.expected_output = "Dire"
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution1().predictPartyVictory(self.senate),
            self.expected_output
        )
        self.assertEqual(
            Solution2().predictPartyVictory(self.senate),
            self.expected_output
        )


class Solution1:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        for senator in senate:
            queue.append(senator=="R")

        while len(queue) > 1:
            senator = queue.popleft()
            try:
                queue.remove(not senator)
            except ValueError:
                break
            queue.append(senator)

        return {
            True: "Radiant",
            False: "Dire",
        }[queue.pop()]


class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue, d_queue = deque(), deque()
        for index, senator in enumerate(senate):
            if senator == "R":
                r_queue.append(index)
            else:
                d_queue.append(index)

        while r_queue and d_queue:
            r_front, d_front = r_queue.popleft(), d_queue.popleft()
            index += 1
            if r_front < d_front:
                r_queue.append(index)
            else:
                d_queue.append(index)

        return "Radiant" if r_queue else "Dire"
                

unittest.main()
