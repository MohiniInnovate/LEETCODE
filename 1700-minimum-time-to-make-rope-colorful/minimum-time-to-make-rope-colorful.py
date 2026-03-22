class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        res = 0
        prev = 0

        for i in range(1, n):
            if colors[i] == colors[prev]:
                if neededTime[i] <= neededTime[prev]:
                    res += neededTime[i]    
                else:
                    res += neededTime[prev]
                    prev = i
            else:
                prev = i 
                
                
                
        return res 
        