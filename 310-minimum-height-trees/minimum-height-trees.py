class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        mat = defaultdict(list)
        
        degree = [0]*n

        for a, b in edges:
            mat[a].append(b)
            mat[b].append(a)
            degree[a] += 1
            degree[b] += 1

        q = deque()

        for d in range(n):
            if degree[d] == 1:
                q.append(d)
        
        nodes = n

        while nodes > 2:
            size = len(q)
            nodes -= size

            for _ in range(size):
                leaf = q.popleft()

                for m in mat[leaf]:
                    degree[m] -= 1
                    if degree[m] == 1:
                        q.append(m)
        return list(q)


            
        

