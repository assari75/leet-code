from collections import deque
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

    @classmethod
    def from_values(cls, values: list):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            if index < len(values) and values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1

            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1

        return root


class Test(unittest.TestCase):

    def test_1(self):
        self.values = [1, 7, 0, 7, -8, None, None]
        self.expected_output = 2
        self.run_test()

    def test_2(self):
        self.values = [989, None, 10250, 98693, -89388, None, None, None, -32127]
        self.expected_output = 2
        self.run_test()

    def run_test(self):
        root = TreeNode.from_values(self.values)
        self.assertEqual(
            Solution().maxLevelSum(root),
            self.expected_output
        )


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        max_level = 1
        level = 1
        queue = deque()
        queue.append(root)
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        return max_level


unittest.main()
