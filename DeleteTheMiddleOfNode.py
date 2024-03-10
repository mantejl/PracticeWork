# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node that will help us keep track of previous node of middle node
        dummy = ListNode(0, head)
        prev = dummy
        slow = head
        fast = head

        # finding the middle node and updating pointers
        while fast and fast.next:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next

            # setting the previous node's next pointer to the node after the middle node
        prev.next = slow.next

        return dummy.next
