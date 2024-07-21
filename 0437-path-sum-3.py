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
        self.values = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
        self.target_sum = 8
        self.expected_output = 3
        self.run_test()

    def test_2(self):
        self.values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        self.target_sum = 22
        self.expected_output = 3
        self.run_test()

    def run_test(self):
        root = TreeNode.from_values(self.values)
        self.assertEqual(
            Solution().pathSum(root, self.target_sum),
            self.expected_output
        )


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0:1}
        self.dfs(root, targetSum, 0, cache)
        return self.result
    
    def dfs(self, root, target, current_path, cache):
        if root is None:
            return  
        current_path += root.val
        old_path = current_path - target
        self.result += cache.get(old_path, 0)
        cache[current_path] = cache.get(current_path, 0) + 1
        
        self.dfs(root.left, target, current_path, cache)
        self.dfs(root.right, target, current_path, cache)
        cache[current_path] -= 1


unittest.main()
