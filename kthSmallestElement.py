# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        # inorder traversal will give us a sorted list
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        # call the function
        inorder(root)
        # and just simply return the kth value
        return values[k - 1]
