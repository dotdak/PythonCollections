def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    visited = {}
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(matrix, i, j, visited))
    return ans
def dfs(matrix, x, y, visited):
    if (x, y) in visited:
        return visited.get((x, y))
    m, n = len(matrix), len(matrix[0])
    path = 1
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    for i, j in move:
        new_x = x + i
        new_y = y + j
        if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
            path = max(path, 1 + self.dfs(matrix, new_x, new_y, visited))
    visited[(x, y)] = path
    return visited[(x, y)]
