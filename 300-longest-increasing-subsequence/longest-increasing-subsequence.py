class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        
        arr = []
        
        for n in nums:
            if not arr or arr[-1] < n:
                arr.append(n)
            else:
                i = bisect_left(arr, n)
                arr[i] = n
        
        return len(arr)

