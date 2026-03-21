class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(m)]

        for a,b in guards:
            mat[a][b] = 'G'
       
        
        for a,b in walls:
            mat[a][b] = 'W'
        
        def helper(i,j, dir):
            if i < 0 or i >= m or j < 0 or j >= n or mat[i][j] == 'G' or mat[i][j] == 'W':
                return 
            mat[i][j] = 1
            if dir == 'd':
                helper(i + 1,j, dir)
            elif dir == 'u':
                helper(i - 1,j, dir)
            elif dir == 'r':
                helper(i,j + 1, dir)
            elif dir == 'l':
                helper(i,j-1, dir)
        

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 'G':
                    helper(r + 1, c, 'd')
                    helper(r-1, c, 'u')
                    helper(r, c + 1, 'r')
                    helper(r, c - 1, 'l')
        res = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    res += 1
        return res

        

        