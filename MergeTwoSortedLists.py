# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two ptr
        ptr1 = list1
        ptr2 = list2

        # creating new LinkedList
        head = ListNode()
        ptr = head

        # while both ptrs are valid
        while ptr1 and ptr2:
            # looping through and the taking the min of the two and increasing the ptrs
            if ptr1.val > ptr2.val:
                ptr.next = ptr2
                ptr2 = ptr2.next
            else:
                ptr.next = ptr1
                ptr1 = ptr1.next
            ptr = ptr.next

        # while loop to get the remaining nodes of the lists
        # can also just set the remaining list to ptr.next instead of looping
        while ptr1 != None:
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next

        while ptr2 != None:
            ptr.next = ptr2
            ptr2 = ptr2.next
            ptr = ptr.next

        return head.next