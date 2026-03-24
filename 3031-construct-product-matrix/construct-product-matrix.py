
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        mod = 12345

        p = [[0] * m for _ in range(n)]

        s = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                p[i][j] = s 
                s = ( s * grid[i][j] ) % mod
    
        pr = 1

            
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * pr )  % mod
                pr = ( pr * grid[i][j] ) % mod
        
        return p
            