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
        self.values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        self.root = TreeNode.from_values(self.values)
        self.p = self.root.left
        self.q = self.root.right
        self.expected_output = self.root
        self.run_test()

    def test_2(self):
        self.values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        self.root = TreeNode.from_values(self.values)
        self.p = self.root.left
        self.q = self.root.left.right.right
        self.expected_output = self.p
        self.run_test()

    def run_test(self):
        self.assertEqual(
            Solution().lowestCommonAncestor(self.root, self.p, self.q),
            self.expected_output
        )


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


unittest.main()
