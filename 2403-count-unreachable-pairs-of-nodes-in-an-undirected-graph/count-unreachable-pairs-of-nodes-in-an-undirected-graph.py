class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        
        par = [i for i in range(n)]
        rank = [1] * (n)

        def find(n1):
            p = par[n1]
            while p != par[p]:
                p = par[par[p]]
            return p

        def union(a,b):
            p1, p2 = find(a), find(b)
            if p1 != p2:
                if rank[p2] > rank[p1]:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                else:
                    par[p2] = p1
                    rank[p1] += rank[p2]

        for a,b in edges:
            union(a,b)
        unreach = 0
        for i in range(n):
            if i == par[i]:
                unreach += ((n - rank[i]) * rank[i] )
        return unreach // 2



        
        
        '''mat = defaultdict(list)

        for a, b in edges:
            mat[a].append(b)
            mat[b].append(a)
        unreach = 0 
        q = deque()
        for i in range(n):
            q.append(i)
            l1 = [j for j in range(n)]
            visit = set(l1)
            return visit
            reach = set()
            while q:
                a = q.popleft()
                reach.add(a)
                visit.remove(a)
                for b in mat[a]:
                    if b not in reach:
                        q.append(b)
                        
            unreach += len(visit)
        return unreach'''
        