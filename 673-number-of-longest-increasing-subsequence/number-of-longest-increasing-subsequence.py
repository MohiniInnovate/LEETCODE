class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        lislen, res = 0, 0
        for i in range(n-1,-1,-1):
            maxlen, maxcount = 1, 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if maxlen < length + 1:
                        maxlen, maxcount = length + 1, count
                    elif maxlen == length + 1:
                        maxcount += count
            dp[i] = (maxlen, maxcount)
            if lislen < maxlen:
                lislen, res = maxlen, maxcount
            elif lislen == maxlen:
                res += maxcount
        
        return res
