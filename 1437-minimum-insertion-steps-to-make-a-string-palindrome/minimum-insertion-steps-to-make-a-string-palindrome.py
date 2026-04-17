class Solution:
    def minInsertions(self, s: str) -> int:
        revs = s[::-1]

        n = len(s)
        if s == revs:
            return 0

        
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == revs[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],  dp[i][j+1])
        
        return n - dp[0][0]

            
