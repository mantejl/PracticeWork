# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, min_val, max_val):
            if not node:
                return True

                # if values of node do not fall in between the proper bounds, it is not a BST
            if not (node.val > min_val and node.val < max_val):
                return False

                # getting the values for the left and right side check
            # setting the boundaries based on what side they are giong on
            l_check = valid(node.left, min_val, node.val)
            r_check = valid(node.right, node.val, max_val)

            return l_check and r_check

        # no restriction on what root value is so it could be anything
        return valid(root, -2 ** 32, 2 ** 32)

        # need to keep track of both min and max values
        # since there might be a case that there is a value less than root
        # inside of the right subtree
        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            for i in range(len(queue)):
                node, lower, upper = queue.popleft()
                if not node:
                    continue

                val = node.val

                # checking if value broke our bounds
                if val <= lower or val >= upper:
                    return False

                # making our values max/min bound respectively based on what side we are going down for
                queue.append((node.left, lower, val))
                queue.append((node.right, val, upper))

        return True
