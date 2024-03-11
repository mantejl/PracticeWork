"""
# Definition for a Node.

"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map old nodes to new nodes so we can set ptrs
        # can't just copy nodes because that won't be a deep copy
        node_map = {None: None}
        curr = head

        # mapping old nodes to new nodes
        while curr:
            node = Node(curr.val)
            node_map[curr] = node
            curr = curr.next

        # passing through loop again to set the pointers
        curr_two = head
        while curr_two:
            new = node_map[curr_two]
            new.next = node_map[curr_two.next] if curr_two.next else None
            new.random = node_map[curr_two.random] if curr_two.random else None
            curr_two = curr_two.next

        return node_map[head]