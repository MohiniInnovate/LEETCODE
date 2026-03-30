class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        stat = defaultdict(list)

        for a, b in connections:
            stat[a].append(b)
            stat[b].append(a)

        online = set()
        station = {}
        heaps = defaultdict(list)

        def dfs(s, g_id):
            if s in online:
                return 
            online.add(s)
            station[s] = g_id
            heappush(heaps[g_id], s)
            for nei in stat[s]:
                dfs(nei, g_id)
        
        for i in range(1, c+1):
            dfs(i,i)
        res = []

        for a, b in queries:
            if a == 1:
                if b in online:
                    res.append(b)
                    continue
                gid = station[b]
                heap = heaps[gid]
                while heap and heap[0] not in online:
                    heappop(heap)
                if heap:
                    res.append(heap[0])
                else:
                    res.append(-1)
            elif a == 2:
                online.discard(b)
        return res

        

        
