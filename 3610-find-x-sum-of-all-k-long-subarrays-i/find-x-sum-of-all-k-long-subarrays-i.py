class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        r = n - k + 1

        ans = [0] * r

        for i in range(r):
            l = i
            r = l + k - 1

            x_count = {}

            for j in range(l, r + 1):
                x_count[nums[j]] = x_count.get(nums[j], 0) + 1
            sorted_count = sorted(x_count.items(), key=lambda t: (-t[1], -t[0]))
            
            if len(sorted_count) < x:
                f = len(sorted_count)
            else:
                f = x
            for key, value in sorted_count[:f]:
                ans[i] += key * value
            
        return ans 