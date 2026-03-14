class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        mat = defaultdict(list)
        i = 0
        for a,b in edges:
            mat[a].append((b, succProb[i]))
            mat[b].append((a, succProb[i]))
            i += 1
        
        q = []

        heapq.heappush(q, (-1, start_node))
        visit = set()
        while q:
            p, t = heapq.heappop(q)
            p = -p
            if t == end_node:
                return p
            visit.add(t)
            for b, prob in mat[t]:
                if b not in visit:
                    heapq.heappush(q, (-(p * prob), b))
        return 0.0

