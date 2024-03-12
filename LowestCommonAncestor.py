# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we are given a binary search tree so we can use that to our advantage
        ptr = root

        while ptr:
            # if the values are greater then we go to the right (common ancestor is on the right side)
            if p.val > ptr.val and q.val > ptr.val:
                ptr = ptr.right
            # if the values are smaller then we go to the left (common ancestor is on the left side)
            elif p.val < ptr.val and q.val < ptr.val:
                ptr = ptr.left
            # if the values are causing a split, then we have found our least common node, so we can return
            else:
                return ptr
