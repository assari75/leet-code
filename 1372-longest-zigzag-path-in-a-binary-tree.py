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
        self.values = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.values = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
        self.expected_output = 4
        self.run_test()

    def run_test(self):
        root = TreeNode.from_values(self.values)
        self.assertEqual(
            Solution().longestZigZag(root),
            self.expected_output
        )


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zigzag = 0
        self.dfs(root, 0, 0)
        return self.longest_zigzag

    def dfs(self, node: Optional[TreeNode], left: int, right: int) -> int:
        self.longest_zigzag = max(self.longest_zigzag, left, right)
        if node.left:
            self.dfs(node.left, right + 1, 0)
        if node.right:
            self.dfs(node.right, 0, left + 1)


unittest.main()
