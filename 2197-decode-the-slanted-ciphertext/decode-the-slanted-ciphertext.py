class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        col = len(encodedText) // rows
        mat = [['']*(col) for _ in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(col):
                mat[i][j] = encodedText[k]
                k += 1
        res = ''

        for c in range(col):
            t = c
            for r in range(rows):
                if t >= col:
                    break
                res += mat[r][t]
                t += 1
        return res.rstrip()



        