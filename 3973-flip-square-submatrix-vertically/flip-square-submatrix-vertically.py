class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        mat = [[0] * k for _ in range(k)]
        r = 0 
        c = 0
        for i in range(x, x + k):
            for j in range(y, y + k):
                mat[r][c] = grid[i][j]
                c += 1
            c = 0
            r += 1
        mat = mat[::-1]
        r = 0 
        c = 0
        for i in range(x,x + k):
            for j in range(y,y + k):
                grid[i][j] = mat[r][c]
                c += 1
            c = 0
            r += 1
        return grid

        
        