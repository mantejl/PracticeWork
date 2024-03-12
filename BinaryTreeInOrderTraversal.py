# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> List[int]:
        # iterative solution
        stack = []
        res = []
        ptr = root

        # while ptr or stack are still non empty
        while ptr or stack:
            # going to absolute left of tree
            while ptr:
                stack.append(ptr)
                ptr = ptr.left
            # popping the most recent valid left node
            ptr = stack.pop()
            # appending it
            res.append(ptr.val)
            # shifting the pointer to the right to traverse right side
            ptr = ptr.right

        return res

        # recursive implementation
        result = []

        # define new function that takes in node
        def inorder(root):
            # if it is null then we return
            if not root:
                return root
            # if not then we process the complete left side of the tree first
            inorder(root.left)
            # then we add the values
            result.append(root.val)
            # then we process the entire right side
            inorder(root.right)

        # call function and return
        inorder(root)
        return result
