# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # updated one pointer with a delay of n steps
        for _ in range(n):
            fast = fast.next

            # taking care of edge case where only one node exists in head
        if fast == None:
            return head.next

        # continue to loop until we have the node to the left of our to-be deleted node and the node to the right
        while fast.next:
            slow = slow.next
            fast = fast.next

        # change the pointers to get rid of that node
        slow.next = slow.next.next

        return head
