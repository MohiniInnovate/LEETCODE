class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)

        ans = [0] * n

        for i in range(n):
            for c in bank[i]:
                if c == '1':
                    ans[i] += 1
        
        res = 0

        for i in range(n):
            if ans[i] != 0:
                l = i
                r = i + 1
                while r < n and ans[r] == 0:
                    r += 1
                if r < n:
                    res += (ans[r] * ans[l])
        return res 
                
                