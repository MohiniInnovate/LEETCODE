class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = set()
        dp.add(0)

        for i in range(n):
            nextDp = set()

            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t+nums[i])
                nextDp.add(t)
            
            dp = nextDp
        
        return False
