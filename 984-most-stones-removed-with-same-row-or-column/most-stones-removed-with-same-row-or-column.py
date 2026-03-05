class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_r = max(s[0] for s in stones)
        max_c = max(s[1] for s in stones)

        par = [i for i in range(max_r + max_c + 2)]
        size = [1] * (max_r + max_c + 2)

        nodes = set()

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
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
        for a, b in stones:
            union(a, b + max_r + 1)
            nodes.add(a)
            nodes.add(b + max_r + 1)
        comp = sum(1 for n in nodes if n == par[n])
        return len(stones) - comp
