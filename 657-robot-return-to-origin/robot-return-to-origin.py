class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        c = 0

        for d in moves:
            if d == 'U':
                r -= 1
            elif d == 'D':
                r += 1
            elif d == 'L':
                c -= 1
            elif d == 'R':
                c += 1
        
        return True if r == 0 and c == 0 else False
             

        