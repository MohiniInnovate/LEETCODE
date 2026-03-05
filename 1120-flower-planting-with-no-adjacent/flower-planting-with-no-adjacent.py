class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        mat = defaultdict(list)

        for a, b in paths:
            mat[a].append(b)
            mat[b].append(a)
        
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            used = set(ans[nei] for nei in mat[i])

            for f in range(1,5):
                if f not in used:
                    ans[i] = f
                    break
        return ans[1:]