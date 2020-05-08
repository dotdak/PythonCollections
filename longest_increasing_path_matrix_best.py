class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not any(matrix): return 0
        m, n = len(matrix), len(matrix[0])
        
        @functools.lru_cache(None)
        def helper(i, j):
            val = matrix[i][j]
            return 1 + max(
                helper(i+1, j) if i < m - 1 and val < matrix[i+1][j] else 0,
                helper(i-1, j) if i and val < matrix[i-1][j] else 0,
                helper(i, j+1) if j < n - 1 and val < matrix[i][j+1] else 0,
                helper(i, j-1) if j and val < matrix[i][j-1] else 0)
        
        return max(helper(i, j) for i in range(m) for j in range(n))
