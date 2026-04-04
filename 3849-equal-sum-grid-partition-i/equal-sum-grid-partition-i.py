class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])

        ans = []

        for r in range(row):
            temp = 0
            for c in range(col):
                temp += grid[r][c]
            ans.append(temp)
        
        tot = sum(ans)
        pref = 0

        for n in ans:
            pref += n
            tot -= n
            if pref == tot:
                return True 
        
        ans = []

        for c in range(col):
            temp = 0
            for r in range(row):
                temp += grid[r][c]
            ans.append(temp)
        
        tot = sum(ans)
        pref = 0

        for n in ans:
            pref += n
            tot -= n
            if pref == tot:
                return True
        return False
        
        
        