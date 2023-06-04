# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur, prev = head, None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

# recursive
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    else:
        recursiveH = reverseList2(head.next)
        head.next.next = head
        head.next = None
        return recursiveH
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    head = result
    while list1 and list2:
        if list1.val <= list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    if list1:
        result.next = list1
    else:
        result.next = list2

    return head.next