class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        res = []
        

        for e in envelopes:
            if not res:
                res.append(tuple(e))
            else:
                w1, h1 = res[-1]
                w2, h2 = e
                if w1 < w2 and h1 < h2 : 
                    res.append(tuple(e))
                else:
                    i = bisect_left(res, h2, key=lambda x: x[1])
                    res[i] = tuple(e)
        return len(res)


        '''
        n = len(envelopes)
        dp = [1] * n
        ans = 0

        for i in range(n-1, -1, -1):
            w1, h1 = envelopes[i]
            res = 0
            for j in range(i+1, n):
                w2, h2 = envelopes[j]
                if w1 < w2 and h1 < h2 :
                    res = max(res, dp[j])
            dp[i] += res
            ans = max(ans, dp[i])
        return ans'''
        