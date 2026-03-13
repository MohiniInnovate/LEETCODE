class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        mat = defaultdict(list)

        for a, b in edges:
            mat[a].append(b)
            mat[b].append(a)

        bt = {} # bob time
        # bob time dfs
        def dfs(src, prev, time):
            if src == 0:
                bt[src] = time
                return True
            for nei in mat[src]:
                if nei != prev:
                    if dfs(nei, src, time + 1):
                        bt[src] = time
                        return True
            return False
        dfs(bob, -1, 0)
        # alice simulation bfs
        q = deque([(0, 0, -1, amount[0])])
        res = float('-inf')
        while q:
            s, t, p, profit = q.popleft()
            for nei in mat[s]:
                if nei != p:
                    na = amount[nei]
                    nt = t + 1
                    if nei in bt: 
                        if nt > bt[nei]:
                            na = 0
                        elif nt == bt[nei]:
                            na = na // 2
                    q.append((nei, nt, s, profit + na))
                    if len(mat[nei]) == 1:
                        res = max(res, profit + na)
                        
                        
        return res    


