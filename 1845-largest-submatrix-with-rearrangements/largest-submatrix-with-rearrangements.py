class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            curr = sorted(matrix[i], reverse=True)
            for k in range(n):
                res = max(res, curr[k] * (k + 1))
        return res
            
            