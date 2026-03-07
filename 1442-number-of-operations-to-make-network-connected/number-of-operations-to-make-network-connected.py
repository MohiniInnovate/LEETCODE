class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        par = [i for i in range(n)]
        size = [1] * (n)

        def find(c):
            p = par[c]

            while p != par[p]:
                p = par[par[p]]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                if size[p1] > size[p2]:
                    par[p2] = p1
                    size[p1] += size[p2]
                else:
                    par[p1] = p2
                    size[p2] += size[p1]


        for a,b in connections:
            union(a,b)
        
        comp = sum(1 for i in range(n) if i == par[i])
        connected = n - comp + 1
        wires_used = connected - 1
        wires_left = len(connections) - wires_used
        wires_needed = comp - 1
        if wires_left >= wires_needed:
            return wires_needed
        return -1 


