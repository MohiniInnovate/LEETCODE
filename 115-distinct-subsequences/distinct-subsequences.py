class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)'''

        n = len(s)
        m = len(t)

        dp = [[0] * (m+1) for _ in range(n+1)]

        
        for r in range(n+1):
            dp[r][m] = 1
        
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if s[r] == t[c]:
                    dp[r][c] = dp[r+1][c+1] + dp[r+1][c]
                else:
                    dp[r][c] = dp[r+1][c]
        return dp[0][0]