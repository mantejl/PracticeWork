from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = set()
    result = []
    while queue:
        node = queue.popleft()
        print("Current Node", node)
        result.append(node)
        for n in graph[node]:
            print("Adjacent Node ", n)
            if n not in visited:
                queue.append(n)
                visited.add(n)

    return result


graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['Z'],
    'D': [],
    'E': ['F'],
    'F': [],
    'Z': []
}
print("Test Case 1:", bfs(graph1, 'A'))
