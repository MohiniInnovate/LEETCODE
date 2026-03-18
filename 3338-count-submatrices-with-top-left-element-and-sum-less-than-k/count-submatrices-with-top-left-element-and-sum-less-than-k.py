class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        tle = grid[0][0]
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n) for _ in range(m) ]

        ans[0][0] = grid[0][0]

        for r in range(m):
            curr = 0 
            for c in range(n):
                ans[r][c] = grid[r][c] 
                if 0 <= r - 1:
                    ans[r][c] += ans[r-1][c]
                ans[r][c] += curr
                curr += grid[r][c] 
        res = 0 
        for r in range(m):
            for c in range(n):
                if ans[r][c] <= k:
                    res += 1
        return res

        

        
