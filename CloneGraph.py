class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        graph = {}
        graph[node] = Node(node.val)
        queue = deque([node])
        
        while queue:
            n = queue.popleft()
            for neigh in n.neighbors:
                if neigh not in graph:
                    graph[neigh] = Node(neigh.val)
                    queue.append(neigh)
                graph[neigh].neighbors.append(graph[n])
        
        return graph[node]

