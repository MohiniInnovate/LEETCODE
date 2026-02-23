class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10**9 + 7
        tot = pow(2, n, mod)
        return (tot - 2) % mod
