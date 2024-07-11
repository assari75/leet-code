from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_val = self.next.val if self.next else None
        return f"ListNode(val={self.val}, next={next_val})"

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
        self.values = [1, 2, 3, 4, 5]
        self.expected_output_values = [1, 3, 5, 2, 4]
        self.run_test()

    def test_2(self):
        self.values = [2, 1, 3, 5, 6, 4, 7]
        self.expected_output_values = [2, 3, 6, 7, 1, 5, 4]
        self.run_test()

    def run_test(self):
        head = ListNode.from_values(self.values)
        expected_output = ListNode.from_values(self.expected_output_values)
        self.assert_linked_lists_equal(
            Solution().oddEvenList(head),
            expected_output
        )

    def assert_linked_lists_equal(self, head1, head2):
        while head1 and head2:
            self.assertEqual(head1.val, head2.val)
            head1 = head1.next
            head2 = head2.next
        self.assertEqual(head1, head2)


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head


unittest.main()
