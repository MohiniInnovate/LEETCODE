class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        mat = defaultdict(list)
        for a,b in richer:
            mat[b].append(a)
        
        ans = [0] * n
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            minv = quiet[i]
            ans[i] = i 

            for a in mat[i]:
                res, b = dfs(a)

                if res <= minv:
                    minv = res
                    ans[i] = b

            dp[i] = (minv, ans[i])
            return dp[i]
        
        for j in range(n):
            dfs(j)
        return ans
        

        
        
        
        
        
        
        '''q = deque()
        for i in range(n):
            q.append(i)
            minv = quiet[i]

            while q:
                r = q.popleft()

                if minv >= quiet[r]:
                    ans[i] = r
                    minv = quiet[r]

                for a in mat[i]:
                    q.append(a)
        return ans'''

                
