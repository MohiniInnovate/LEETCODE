class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        f = defaultdict(list)
        
        q = deque()

        visit = set()

        q.append((id, 0))


        ans = []
        visit.add(id)
        freq = {}

        while q:
            fr, d = q.popleft()

            if d == level:
                ans.append(fr)
                continue
        
            for a in friends[fr]:
                if a not in visit:
                    q.append((a, d + 1 ))
                    visit.add(a)
        for n in ans:
            for c in watchedVideos[n]:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1
        sorted_ans = dict(sorted(freq.items(), key=lambda item: (item[1], item[0])))
        return list(sorted_ans.keys())
        
        


        
        