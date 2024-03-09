# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        # three pointers that track the current states
        curr_ptr = head
        prev = None

        # looping through each ptr of original linkedlist
        while curr_ptr:
            # getting next node
            next_ptr = curr_ptr.next
            # starting the reverse process
            curr_ptr.next = prev
            # setting prev to current pointer
            prev = curr_ptr
            # setting current ptr to next ptr
            curr_ptr = next_ptr

        return prev