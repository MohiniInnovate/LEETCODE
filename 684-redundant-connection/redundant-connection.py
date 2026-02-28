class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(0, n+1)]
        rank = [1] * (n+1)

        def find(n):
            p = par[n]

            while p != par[p]:
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return False

        for n1, n2 in edges:
            if union(n1,n2):
                return [n1,n2]


        