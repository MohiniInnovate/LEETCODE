class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = defaultdict(list)

        for u,v,w in times:
            mat[u].append((v,w))
        

        q = [(0,k)]

        res = 0

        visit = set()
        
        
        while q:
            w1, src = heapq.heappop(q)
            if src in visit:
                continue
            visit.add(src)
            res = w1
            for v, w2 in mat[src]:
                if v not in visit:
                    heapq.heappush(q, (w2 + w1, v))
        if len(visit) == n:
            return res
        else:
            return -1




