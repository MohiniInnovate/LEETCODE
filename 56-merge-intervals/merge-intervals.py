class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inter = sorted(intervals, key=lambda x:x[0])
        res = []
        res.append(inter[0])

        for s,e in inter[1:]:
            t = res[-1][1]

            if s <= t:
                n = max(t, e)
                res[-1][1] = n
            else:
                res.append([s,e])
        return res
