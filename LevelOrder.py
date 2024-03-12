# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # simple BFS algorithm
        if not root:
            return []

        q = deque([root])
        res = []

        # while the queue exists
        while q:
            tmp = []
            # loop through the number of elements in the queue
            for i in range(len(q)):
                # pop it off
                node = q.popleft()
                # add children if valid
                if node:
                    # add node to tmp array
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # as long as there is something in tmp then we are adding it to our result array
            if len(tmp) > 0:
                res.append(tmp)

        return res


