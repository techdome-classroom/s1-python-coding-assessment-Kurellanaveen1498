def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(i, j):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            grid[x][y] = 'W'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'L':
                    stack.append((nx, ny))
    
    island_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L':
                # We found an unvisited land cell, start DFS to mark the entire island
                island_count += 1
                dfs(i, j) 
    
    return island_count
