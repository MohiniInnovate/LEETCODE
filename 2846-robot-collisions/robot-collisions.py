class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        pos = {}

        for i, p in enumerate(positions):
            pos[p] = i
        
        sort_pos = dict(sorted(pos.items(), key=lambda x:x[0]))

        for p, v in sort_pos.items():
            d1 = directions[v]
            h1 = healths[v]
            if d1 == 'L':
                p = (-1) * p
            if stack and stack[-1][0] != d1 and stack[-1][2] + p < 0:
                flag = 0
                while stack and stack[-1][0] != d1 and flag == 0 and stack[-1][2] + p < 0:
                    h =  stack[-1][1]
                    if h > h1:
                        stack[-1][1] = h - 1
                        flag = 1
                    elif h < h1:
                        stack.pop()
                        h1 = h1 - 1
                    else:
                        stack.pop()
                        flag = 1
                if flag == 0:
                    stack.append([d1, h1, p, v])
            else:
                stack.append([d1, h1, p, v])
        
        res = sorted(stack, key=lambda x:x[3])

        
        
        return [i[1] for i in res]
        