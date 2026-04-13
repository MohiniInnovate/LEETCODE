class Solution:
    def numDistinct(self, s: str, t: str) -> int:
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