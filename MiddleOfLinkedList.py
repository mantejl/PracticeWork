# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head

        # slow pointer and fast pointer
        slow = head
        fast = head

        # taking care of both even node and odd node length lists with these two checks
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # return
        return slow