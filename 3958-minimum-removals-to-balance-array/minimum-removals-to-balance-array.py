class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        right = 0
        ans = n

        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            ans = min(ans, n - (right - left))
        return ans
        