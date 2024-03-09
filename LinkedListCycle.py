# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow pointer, fast pointer approach

        # quicker method wtihout additional checks
        # slow = head
        # fast = head

        # while fast != None and fast.next != None:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True

        # return False

        if head == None:
            return False

        slow_ptr = head
        fast_ptr = head

        # setting first
        if (fast_ptr.next):
            fast_ptr = head.next.next

        while fast_ptr and fast_ptr.next != None:
            if slow_ptr == fast_ptr:
                return True
            else:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

        return False

