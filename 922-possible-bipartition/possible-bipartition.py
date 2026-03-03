class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        rank = [1] * (n+1)
        par  = [i for i in range(n+1)]
        mat = defaultdict(list)

        for a, b in dislikes:
            mat[a].append(b)
            mat[b].append(a)

        def find(d):
            p = par[d]

            while p != par[p]:
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
        
        def check(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            return True


        for d in range(1, n+1):
            for i in range(len(mat[d])):
                if i + 1 < len(mat[d]):
                    union(mat[d][i], mat[d][i+1])
        for n1, n2 in dislikes:
            if not check(n1, n2):
                return False
        return True 