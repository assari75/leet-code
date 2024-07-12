from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

    @classmethod
    def from_values(cls, values: list):
        if not values:
            return None
        head = ListNode(values[0])
        node = head
        for value in values[1:]:
            node.next = ListNode(value)
            node = node.next
        return head


class Test(unittest.TestCase):

    def test_1(self):
        self.values = [5, 4, 2, 1]
        self.expected_output = 6
        self.run_test()

    def test_2(self):
        self.values = [4, 2, 2, 3]
        self.expected_output = 7
        self.run_test()

    def test_3(self):
        self.values = [1, 100000]
        self.expected_output = 100001
        self.run_test()

    def run_test(self):
        head = ListNode.from_values(self.values)
        self.assertEqual(
            Solution().pairSum(head),
            self.expected_output
        )


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half_head = slow.next
        slow.next = None
        reversed_second_half_head = self.reverseList(second_half_head)
        first_half_node = head
        second_half_node = reversed_second_half_head
        maximum = first_half_node.val + second_half_node.val
        while first_half_node.next:
            first_half_node = first_half_node.next
            second_half_node = second_half_node.next
            maximum = max(maximum, first_half_node.val + second_half_node.val)
        return maximum

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        current_node = head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node


unittest.main()
