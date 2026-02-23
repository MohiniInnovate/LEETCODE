class Solution:
    def lastInteger(self, n: int) -> int:
        l1 = range(1,n+1)

        while len(l1) != 1:
            l1 = l1[0::2]
            l1 = l1[::-1]
        return l1[0]