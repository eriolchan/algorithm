from typing import List


class ListNode(object):
    """Definition for singly-linked list."""

    def __init__(self, value: int) -> None:
        self.val = value
        self.next = None

    def __eq__(self, other: any) -> bool:
        if isinstance(other, self.__class__):
            return self.val == other.val
        return False

    @classmethod
    def build_linked_list(cls, values: List[int]) -> 'ListNode':
        head = None
        previous = None
        for value in values:
            node = ListNode(value)
            if not head:
                head = node
            if previous:
                previous.next = node
            previous = node
        return head

    @classmethod
    def linked_list_equal(cls, first: 'ListNode', second: 'ListNode') -> bool:
        while first and second and first == second:
            first = first.next
            second = second.next
        return first == second
