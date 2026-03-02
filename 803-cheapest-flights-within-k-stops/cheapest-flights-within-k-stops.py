class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mat = defaultdict(list)
        for f,t,p in flights:
            mat[f].append((t,p))

        q = [(0, 0, src)]
        res = float('inf')
        visit = set()
        
        while q:
            p1, st, s1 = heapq.heappop(q)
            if s1 == dst:
                res = min(res, p1)
                continue
            if (s1, st) in visit or st > k:
                continue
            visit.add((s1, st))
            for t1, p2 in mat[s1]:
                if  (t1, st + 1) not in visit:
                    heapq.heappush(q, (p2 + p1, st + 1, t1))
        return res if res != float('inf') else -1

            
        '''def dfs(src, p, stops):
            if src == dst:
                return p
            if (src, stops) in dp:
                return dp[(src, stops)]
            res = float('inf')
            if stops <= k:
                for t1, p2 in mat[src]:
                    res = min(res, dfs(t1, p + p2, stops + 1))
            dp[(src, stops)] = res
            return dp[(src, stops)]
        r = dfs(src, 0, 0)
        return r if r != float('inf') else -1'''