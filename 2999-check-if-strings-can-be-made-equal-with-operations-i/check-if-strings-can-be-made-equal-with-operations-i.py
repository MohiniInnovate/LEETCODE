class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def equal(s, i):
            if s == s2:
                return True
            if i == 2:
                return False
            
            # not swaping
            if equal(s, i + 1):
                return True
            # swaping
            t1 = list(s)
            c1 = s1[i]
            c2 = s1[i+2]
            t1[i] = c2
            t1[i+2] = c1
            t1 = ''.join(t1)

            if equal(t1, i+1):
                return True
            
            return False
        return equal(s1, 0)