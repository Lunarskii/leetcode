from typing import Optional


"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    Output: [7, 0, 8]
    Explanation: 342 + 465 = 807.
Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
Example 3:
    Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    Output: [8, 9, 9, 9, 0, 0, 0, 1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: list[int], *, reverse: bool = True) -> ListNode:
    if reverse:
        values.reverse()
    node = None
    for value in values:
        node = ListNode(val=value, next=node)
    return node


def compare_linked_lists(l1: ListNode, l2: ListNode) -> bool:
    while l1 or l2:
        if (l1 and not l2) or (l2 and not l1):
            return False
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


def print_linked_list(l: ListNode) -> None:
    while l:
        print(l.val)
        l = l.next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry: int = 0
    head = ListNode(0)
    tail = head

    while l1 or l2 or carry:
        l1_value, l1 = (l1.val, l1.next) if l1 else (0, None)
        l2_value, l2 = (l2.val, l2.next) if l2 else (0, None)

        summ = l1_value + l2_value + carry
        rest = summ % 10
        carry = summ // 10

        tail.next = ListNode(val=rest)
        tail = tail.next
    return head.next


if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    res = create_linked_list([7, 0, 8])
    assert compare_linked_lists(add_two_numbers(l1, l2), res)

    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    res = create_linked_list([0])
    assert compare_linked_lists(add_two_numbers(l1, l2), res)

    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    res = create_linked_list([8, 9, 9, 9, 0, 0, 0, 1])
    assert compare_linked_lists(add_two_numbers(l1, l2), res)
