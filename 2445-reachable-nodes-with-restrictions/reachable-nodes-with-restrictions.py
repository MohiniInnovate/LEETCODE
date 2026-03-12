class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = set(restricted)

        q = deque()

        mat = defaultdict(list)

        for a,b in edges:
            mat[a].append(b)
            mat[b].append(a)

        visit = set()
        visit.add(0)

        q.append(0)

        ans = 0

        while q:
            a = q.popleft()
            ans += 1
            for b in mat[a]:
                if b not in res and b not in visit:
                    q.append(b)
                    visit.add(b)
        return ans



        