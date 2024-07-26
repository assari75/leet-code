from collections import deque
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.inputs = [1, 100, 3001, 3002]
        self.expected_outputs = [1, 2, 3, 3]
        self.run_test()

    def test_2(self):
        self.inputs = [642, 1849, 4921, 5936, 5957]
        self.expected_outputs = [1, 2, 1, 2, 3]
        self.run_test()

    def run_test(self):
        recent_counter = RecentCounter()
        outputs = []
        for input in self.inputs:
            output = recent_counter.ping(input)
            outputs.append(output)
        self.assertEqual(outputs, self.expected_outputs)


class RecentCounter:

    def __init__(self):
        self.recent_calls = deque()
        self.counter = 0
        self.recent_time = 3000

    def ping(self, t: int) -> int:
        self.recent_calls.append(t)
        self.counter += 1
        while self.recent_calls[0] < t - self.recent_time:
            self.recent_calls.popleft()
            self.counter -= 1
        return self.counter
            

unittest.main()
