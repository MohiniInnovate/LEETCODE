class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        i = 0
        while num < n:
            num = pow(3, i)
            i += 1
        return True if num == n else False