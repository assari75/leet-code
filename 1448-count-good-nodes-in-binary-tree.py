from collections import deque
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
        self.values = [3, 1, 4, 3, None, 1, 5]
        self.expected_output = 4
        self.run_test()

    def test_2(self):
        self.values = [3, 3, None, 4, 2]
        self.expected_output = 3
        self.run_test()

    def test_3(self):
        self.values = [1]
        self.expected_output = 1
        self.run_test()

    def run_test(self):
        root = TreeNode.from_values(self.values)
        self.assertEqual(
            Solution().goodNodes(root),
            self.expected_output
        )


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root, root.val)

    def count_good_nodes(self, root: TreeNode, max_val: int) -> int:
        if not root:
            return 0
        count = 0
        if root.val >= max_val:
            count += 1
            max_val = root.val
        count += self.count_good_nodes(root.left, max_val)
        count += self.count_good_nodes(root.right, max_val)
        return count


unittest.main()
