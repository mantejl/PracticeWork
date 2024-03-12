# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # adding a reversed list
        if not root:
            return
        queue = deque([root])
        result = []
        level = 0

        # standard BFS
        while queue:
            nodes = []
            for i in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # checking which list to add to result
            if level % 2 == 0:
                result.append(nodes)
            else:
                result.append(reversed(nodes))
            level += 1

        return result

        if not root:
            return

        # queue for BFS and a stack for odd levels
        queue = deque([root])
        stack = []
        res = []
        level = 0

        while queue:
            tmp = []
            # if level is even, normal BFS
            if level % 2 == 0:
                for i in range(len(queue)):
                    node = queue.popleft()
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            # if not, then pop the elements using a stack and add them to the tmp array
            else:
                for i in range(len(queue)):
                    node = queue.popleft()
                    stack.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                while stack:
                    tmp.append(stack.pop().val)
            # increment level and add tmp to result list
            level += 1
            res.append(tmp)

        return res