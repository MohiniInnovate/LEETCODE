class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        mat = collections.defaultdict(list)
        

        for a,b in connections:
            mat[a].append(b)
            mat[b].append(a)
            

        res = []
        low = [-1] * n
        disc = [-1] * n
        
        def dfs(u, p, t):
            disc[u] = low[u] = t
            t += 1

            for v in mat[u]:
                if v == p:
                    continue
                if disc[v] == -1:
                    dfs(v, u, t)

                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        res.append([u,v])
                else:
                    low[u] = min(low[u], disc[v])
        dfs(0, -1, 0)
        return res




        