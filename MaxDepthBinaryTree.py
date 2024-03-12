# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs with queue
        queue = deque([root])
        max_val = 0

        if not root:
            return 0

        # while queue still exists
        while queue:
            # get every possible node available at that level
            for i in range(len(queue)):
                # add it's children to the queue
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # we have gone down one level, so increment value
            max_val += 1

        return max_val

        # recursive solution
        if not root:
            return 0

            # continue to run the same method on the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # since empty node returns 0, we can add one everytime
        return 1 + max(left_depth, right_depth)
