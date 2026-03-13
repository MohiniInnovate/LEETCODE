class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mat = defaultdict(set)

        for a, b in prerequisites:
            mat[b].add(a)

        res = []

        for u, v in queries:
            q = deque()
            q.append(v)
            visit = set()
            while q:
                a = q.popleft()
                if a == u:
                    res.append(True)
                    break
                visit.add(a)
                for b in mat[a]:
                    if b not in visit:
                        q.append(b)
            if a != u:
                res.append(False)
        return res


        