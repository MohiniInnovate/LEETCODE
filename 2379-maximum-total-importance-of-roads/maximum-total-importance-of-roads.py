class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        mat = defaultdict(list)
        degree = {}

        for a, b in roads:
            mat[a].append(b)
            mat[b].append(a)
            degree[a] = degree.get(a, 0) + 1
            degree[b] = degree.get(b, 0) + 1

        sorted_degree = dict(sorted(degree.items(), key = lambda X: -X[1]))
        ans = [0] * n
        t = n
        for a in sorted_degree:
            ans[a] = t 
            t -= 1
        fullsum = 0
        for a,b in roads:
            fullsum += ans[a] + ans[b]
        return fullsum




        
        
        
