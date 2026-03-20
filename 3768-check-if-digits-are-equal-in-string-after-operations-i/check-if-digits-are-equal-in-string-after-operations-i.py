class Solution:
    def hasSameDigits(self, s: str) -> bool:
        new_s = ''
        while len(s) != 2:
            for i in range(1, len(s)):
                new_s += str(((int(s[i]) + int(s[i-1])) % 10))
            s = new_s
            new_s = ''
        if s[0] == s[1]:
            return True
        return False
