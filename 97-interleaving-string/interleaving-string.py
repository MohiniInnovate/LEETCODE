class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)

        if m + n != o:
            return False

        dp = {}

        def dfs(i,j,k):
            if i == m and j == n and k < o:
                return i,j,k
            if i == m and j == n and  k == o:
                return True
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            r1 = False
            r2 = False
            if i < m and s1[i] == s3[k]:
                r1 = dfs(i+1,j,k+1)
            if j < n and s2[j] == s3[k]:
                r2 = dfs(i,j+1,k+1)            
            dp[(i,j,k)] =  r1 or r2
            return dp[(i,j,k)]
        return dfs(0,0,0)
             