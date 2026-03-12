class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        q = deque()
        q.append((node1,0))
        ans1 = {}
        while q:
            a, d = q.popleft()
            if a in ans1:
                ans1[a] = min(ans1[a], d)
            else:
                ans1[a] = d
            b = edges[a]
            if b != -1:
                if ( b in ans1 and ans1[b] > d + 1 ) or b not in ans1:
                    q.append((b, d + 1))
        q.append((node2,0))
        ans2 = {}
        while q:
            a, d = q.popleft()
            if a in ans2:
                ans2[a] = min(ans2[a], d)
            else:
                ans2[a] = d
            b = edges[a]
            if b != -1:
                if ( b in ans2 and ans2[b] > d + 1 ) or b not in ans2:
                    q.append((b, d + 1))
        min_dis = float('inf')
        ans = -1
        sor_a1 = dict(sorted(ans1.items(), key=lambda x: (x[1], x[0])))
        for a in sor_a1:
            if a in ans2:
                max_d = max(sor_a1[a], ans2[a])
                if max_d < min_dis:
                    min_dis = max_d
                    ans = a
                elif max_d == min_dis and ans > a:
                    min_dis = max_d
                    ans = a
        return ans 
        

