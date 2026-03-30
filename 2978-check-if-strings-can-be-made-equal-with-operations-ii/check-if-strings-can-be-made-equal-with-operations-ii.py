class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a = sorted([c for c in s1[0::2]])
        b = sorted([c for c in s2[0::2]])
        c = sorted([c for c in s1[1::2]])
        d = sorted([c for c in s2[1::2]])

        return a == b and c == d
        