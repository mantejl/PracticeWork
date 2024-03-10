# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from BinaryNumToDecimal import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr = slow
        prev = None

        # reverse the second half of the linked list
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt

        # merge both of the halves
        # creating new node and merging

        final_ptr = head
        final_ptr2 = prev
        node = ListNode()
        node_ptr = node
        count = 0

        while final_ptr and final_ptr2:
            if count % 2 == 0:
                node_ptr.next = final_ptr
                final_ptr = final_ptr.next
                node_ptr = node_ptr.next
                count += 1
            else:
                node_ptr.next = final_ptr2
                final_ptr2 = final_ptr2.next
                node_ptr = node_ptr.next
                count += 1

        if final_ptr:
            node.next = final_ptr
        else:
            node.next = final_ptr2

        return node
