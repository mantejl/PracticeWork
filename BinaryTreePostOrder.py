# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # two stacks
        # one for nodes and one more for whether node has been visited
        stack = [root]
        visited = [False]
        res = []
        while stack:
            # get the node and it's visited status
            node = stack.pop()
            visit = visited.pop()
            # if the node is valid and been visited add to list
            if node:
                if visit:
                    res.append(node.val)
                else:
                    # if it's a new node, then add the node and it's 2 children
                    # along with their visited status to the stacks
                    stack.append(node)
                    visited.append(True)
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)

        return res

        # very similar to other traversals
        res = []

        # we iterate left and right before returning
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)

        postOrder(root)
        return res