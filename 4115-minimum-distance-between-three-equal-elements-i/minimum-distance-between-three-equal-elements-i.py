class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        element = set()

        for i, n in enumerate(nums):
            indices[n].append(i)
            if len(indices[n]) >= 3 and n not in element:
                element.add(n)
        
        res = float('inf')

        for n in element:
            a = 0
            while a + 2 < len(indices[n]):
                i,j,k = indices[n][a:a+3]
                res = min(res, abs(i-j) + abs(j-k) + abs(k-i))
                a += 1
        
        return res if res != float('inf') else -1