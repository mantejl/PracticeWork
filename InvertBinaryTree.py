# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None

        # grabbing the node's childrens
        nodel = root.left if root.left else None
        noder = root.right if root.right else None

        # swapping the left with the right and the right with the left
        root.left = noder
        root.right = nodel

        # recursively inverting both the left side of the tree and the right side of the tree
        self.invertTree(nodel)
        self.invertTree(noder)

        # returning the root
        return root

