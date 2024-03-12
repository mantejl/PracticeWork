# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return

            # the first value of the preorder list will always be our root node
        node = TreeNode(preorder[0])
        # finding the index of that root node in our inorder list
        index = inorder.index(node.val)
        # we want all of the values left of the index since that is our pre order graph
        # we want all the values left of in order since we are creating the left subtree
        node.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        # we want all of the values right of the index since that is our pre order graph
        # preorder goes node, left, right
        # we want all the values left of in order since we are creating the right subtree
        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return node