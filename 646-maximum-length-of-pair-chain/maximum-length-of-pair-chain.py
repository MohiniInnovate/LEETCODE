class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        p = sorted(pairs, key=lambda x:x[0])
        n = len(pairs)
        dp = [1] * n 
        ans = 0
        for i in range(n-1,-1,-1):
            res = 0
            a,b = p[i]
            for j in range(i+1,n):
                c,d = p[j]
                if b < c :
                    res = max(res, dp[j])
            dp[i] += res

            ans = max(ans, dp[i])
        return ans 
