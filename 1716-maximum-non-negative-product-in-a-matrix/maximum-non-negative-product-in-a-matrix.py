class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = {}

        m = len(grid)
        n = len(grid[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                temp = grid[i][j]
                if j + 1 < n and i + 1 < m:
                    dmax, dmin = dp[(i+1,j)]
                    rmax, rmin = dp[(i,j+1)]                    
                    dp[(i,j)] = (max(temp * dmax, temp * dmin, temp * rmax, temp * rmin),  min(temp * dmax, temp * dmin, temp * rmax, temp * rmin))
                elif i + 1 < m:
                    dmax, dmin = dp[(i+1,j)]
                    dp[(i,j)] = (max(temp * dmax, temp * dmin), min(temp * dmax, temp * dmin))
                elif j + 1 < n:
                    rmax, rmin = dp[(i,j+1)]
                    dp[(i,j)] = (max(temp * rmax, temp * rmin),  min(temp * rmax, temp * rmin))
                else:
                    dp[(i,j)] = (temp, temp)
        ans = max(dp[(0,0)])
        if ans < 0:
            return -1
        return ans % (10**9 + 7)