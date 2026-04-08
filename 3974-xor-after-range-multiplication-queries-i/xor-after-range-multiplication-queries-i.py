class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        for q in queries:
            l, r, k, v = q
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % (10**9 + 7 )
                i += k
        res = nums[0]

        for n in nums[1:]:
            res ^= n
        return res
        
            