class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = {}
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-1, -1, -1):
            temp = []
            res = [nums[i]]
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    if len(res) < len(temp):
                        res = temp
            dp[i] = res
            if len(ans) < len(res):
                ans = res
        return ans 
            
