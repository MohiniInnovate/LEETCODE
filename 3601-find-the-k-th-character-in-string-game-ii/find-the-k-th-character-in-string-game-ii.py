class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        length = pow(2, n-1)
        cnt = 0
        for i in range(n-1,-1,-1):
            if k > length:
                k -= length
                if operations[i] == 1:
                    cnt += 1
            length = length // 2
        return chr(ord('a') + cnt % 26)