class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        n = len(nums)
        dp = [1] * (n)
        ans = 0

        for i in range(n-1,-1,-1):
            res = 0
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    res = max(res, dp[j])
            dp[i] += res
            ans = max(ans, dp[i])
        
        return ans

