def dfs(graph, start):
    stack = [start]
    visited = set()
    result = []
    while stack:
        node = stack.pop()
        result.append(node)
        print("Current Node", node)
        for n in graph[node]:
            if n not in visited:
                print("Checking node", n)
                visited.add(n)
                stack.append(n)

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
print("Test Case 1:", dfs(graph1, 'A'))
