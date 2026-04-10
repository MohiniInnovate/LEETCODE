class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size = 1
        index = 0

        for i in range(1,n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            if max_size < dp[i]:
                max_size = dp[i]
                index = i

        curr = nums[index]
        s = max_size
        res = []

        for i in range(index, -1, -1):
            if curr % nums[i] == 0 and dp[i] == s:
                res.append(nums[i])
                curr = nums[i]
                s -= 1
        return res

         
            
