class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for u, v , w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # floyd warshall algo
        # you have to check if a shortest path between two nodes exist by going from
        # i - k - j
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        minreachablecity = float('inf')
        bestcity = -1
        
        for i in range(n):
            reachablecity = 0

            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachablecity += 1
            if reachablecity <= minreachablecity:
                minreachablecity = reachablecity
                bestcity = i
        return bestcity


        