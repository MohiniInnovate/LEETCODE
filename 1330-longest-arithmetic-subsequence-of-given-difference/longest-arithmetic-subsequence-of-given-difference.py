class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}

        longest = 1

        for n in arr:
            dif = n - difference
            if dif in dp:
                dp[n] = dp[dif] + 1
            else:
                dp[n] = 1

            longest = max(longest, dp[n])
                    
        return longest