class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        def dfs(i,j, p):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= p:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            c = matrix[i][j]
            dp[(i,j)] =  1 + max(dfs(i+1,j,c), dfs(i-1,j,c), dfs(i,j+1,c), dfs(i,j-1,c))
            return dp[(i,j)]
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r,c,-1))
        return res
