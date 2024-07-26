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
        self.values1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
        self.values2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
        self.expected_output = True
        self.run_test()

    def test_2(self):
        self.values1 = [1, 2, 3]
        self.values2 = [1, 3, 2]
        self.expected_output = False
        self.run_test()

    def test_3(self):
        self.values1 = [1, 2]
        self.values2 = [2, 2]
        self.expected_output = True
        self.run_test()

    def run_test(self):
        root1 = TreeNode.from_values(self.values1)
        root2 = TreeNode.from_values(self.values2)
        self.assertEqual(
            Solution().leafSimilar(root1, root2),
            self.expected_output
        )


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf_values = self.get_leaf_values(root1)
        root2_leaf_values = self.get_leaf_values(root2)
        return root1_leaf_values == root2_leaf_values

    def get_leaf_values(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.get_leaf_values(root.left) + self.get_leaf_values(root.right)


unittest.main()
