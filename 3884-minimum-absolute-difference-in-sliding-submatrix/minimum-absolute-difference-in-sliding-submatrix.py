class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ans = [[0] * (n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                visit = set()
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        visit.add(grid[x][y])
                visit = list(visit)
                min_n = float('inf')
                visit.sort()
                for t in range(1, len(visit)):
                    min_n = min(min_n, abs(visit[t] - visit[t-1]))
                if min_n != float('inf'):
                    ans[i][j] = min_n
        return ans
