from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs approach, recursive
        row = len(grid)
        col = len(grid[0])
        islands = 0
        visited = set()

        # dfs algo
        def dfs(r, c):
            # checking base conditions
            if (r not in range(row) or
                    c not in range(col) or
                    grid[r][c] != "1" or
                    (r, c) in visited
            ):
                return

            # adding cell to visited
            visited.add((r, c))

            # running dfs with new row and col values
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # calling dfs for cells that are valid
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands

        # bfs solution
        if not grid:
            return 0

            # getting boundaries and visited set
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        # standard bfs
        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            # different from trees
            while queue:
                cell = queue.popleft()
                row = cell[0]
                col = cell[1]
                # getting all possible directions that we can have from one cell
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                # looping through each possiblity and creating new rows/cols to run bfs on if valid
                for r, c in directions:
                    new_r = row + r
                    new_c = col + c
                    # creating new row/col numbers
                    if (new_r in range(rows) and
                            new_c in range(cols) and
                            (new_r, new_c) not in visited and
                            grid[new_r][new_c] == "1"):
                        # if new cell is valid (in bounds, not visited, equal to one) then add to queue and visited set
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        # looping through each cell and checking if it's a 1 and not in visited
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # if that's the case then we can run bfs on it and increment the number of islands
                    bfs(i, j)
                    islands += 1
        return islands

