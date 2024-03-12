# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base condition if both nodes are empty
        if not p and not q:
            return True

        # another base condition if the values of the 2 nodes are not the same
        if not p or not q or p.val != q.val:
            return False

        # recursively check the left nodes of both trees and the right nodes of both trees
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))