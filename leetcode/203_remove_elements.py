"""Remove Linked List Elements.

Remove all elements from a linked list of integers that have value val.

https://leetcode.com/problems/remove-linked-list-elements/

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""


from data_structure.list_node import ListNode
import unittest


class Solution(object):

    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        previous, current = sentinel, head
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return sentinel.next


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_remove_multiple(self):
        head = ListNode.build_linked_list([1, 2, 6, 3, 4, 5, 6])
        expect = ListNode.build_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(self.solution.remove_elements(head, 6), expect)

    def test_remove_no_element(self):
        head = ListNode.build_linked_list([1, 2, 3, 4])
        self.assertEqual(self.solution.remove_elements(head, 5), head)

    def test_remove_middle(self):
        head = ListNode.build_linked_list([1, 2, 3, 4])
        expect = ListNode.build_linked_list([1, 3, 4])
        self.assertEqual(self.solution.remove_elements(head, 2), expect)

    def test_remove_head(self):
        head = ListNode.build_linked_list([1, 2, 3, 4])
        expect = ListNode.build_linked_list([2, 3, 4])
        self.assertEqual(self.solution.remove_elements(head, 1), expect)

    def test_remove_tail(self):
        head = ListNode.build_linked_list([1, 2, 3, 4])
        expect = ListNode.build_linked_list([1, 2, 3])
        self.assertEqual(self.solution.remove_elements(head, 4), expect)

    def test_remove_none(self):
        head = None
        self.assertIsNone(self.solution.remove_elements(head, 1))

    def test_remove_same(self):
        head = ListNode.build_linked_list([1, 1, 1])
        self.assertIsNone(self.solution.remove_elements(head, 1))


if __name__ == '__main__':
    unittest.main()
