class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # starting point 
        x, y = 0, 0 

        # tracking the direction 

        direct = [[0,1], [1,0], [0, -1], [-1, 0]] # N E S W Clock wise direction 

        # making a hashset to track obstacles
        obs = {tuple(o) for o in obstacles}

        # direction and index of the direct
        d = 0

        res = 0

        for c in commands:
            if c == -1: # clockwise direction, so we are adding the index, like moving index forward
                d = ( d + 1 ) % 4 # we are doing modulus 4 to keep the index inbounds
            elif c == -2: # going clockwise direction/ moving the index backward
                d = (d - 1) % 4
            else:
                dx, dy = direct[d]
                for _ in range(c): # adding one by one to track obstacles
                    if (x+dx, y+dy) in obs:
                        break
                    x, y = x + dx, y + dy
            res = max(res, x**2 + y**2)
        return res



        