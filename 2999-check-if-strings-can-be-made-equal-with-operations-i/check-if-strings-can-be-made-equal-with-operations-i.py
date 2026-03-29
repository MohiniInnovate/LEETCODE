class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a = sorted([s1[0], s1[2]])
        b = sorted([s1[1], s1[3]])
        c = sorted([s2[0], s2[2]])
        d = sorted([s2[1], s2[3]])

        return a == c and b == d
        
        
        
        
        
        
        
        
        
        '''def equal(s, i):
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
        return equal(s1, 0)'''