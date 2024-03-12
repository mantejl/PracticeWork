# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution with stack, ptr and result list
        stack = []
        res = []
        ptr = root

        # while ptr or stack are still valid
        while ptr or stack:
            # if the ptr is not null, then we add it to our list
            # and then add the right pointer to our stack since that's the
            # node that we want to check right away after we reach the left
            # most node
            if ptr:
                res.append(ptr.val)
                stack.append(ptr.right)
                ptr = ptr.left
            else:
                # if the current node is null, we just pop from the stack
                ptr = stack.pop()

        # return res
        return res

        # same concept as inorder
        res = []

        # except in this case we are adding the values to our result list first and then
        # searching through the rest of the tree
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
