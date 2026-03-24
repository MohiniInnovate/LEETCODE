class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)

        for i in range(n-1, -1, -1):
            dp[i] = nums[i]
            for j in range(i+2, n):
                dp[i] = max(dp[i], nums[i] + dp[j])
        return max(dp)
