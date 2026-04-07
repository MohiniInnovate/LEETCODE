class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        res = []
        

        for w, h in envelopes:
            i = bisect_left(res,h)
            if i == len(res):
                res.append(h)
            else:
                res[i] = h
        return len(res)
            