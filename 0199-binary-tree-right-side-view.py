from collections import deque
from typing import Optional, List
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
        self.values = [1, 2, 3, None, 5, None, 4]
        self.expected_output = [1, 3, 4]
        self.run_test()

    def test_2(self):
        self.values = [1, None, 3]
        self.expected_output = [1, 3]
        self.run_test()

    def test_3(self):
        self.values = []
        self.expected_output = []
        self.run_test()

    def test_4(self):
        self.values = [1, 2, 3, 4]
        self.expected_output = [1, 3, 4]
        self.run_test()

    def run_test(self):
        root = TreeNode.from_values(self.values)
        self.assertEqual(
            Solution().rightSideView(root),
            self.expected_output
        )


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node, level):
            if not node:
                return
            if len(output) < level:
                output.append(node.val)
            traverse(node.right, level + 1)
            traverse(node.left, level + 1)
        
        output = []
        traverse(root, 1)
        return output


unittest.main()
