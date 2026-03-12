class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        ans = [0] * (n)

        for i,a in enumerate(edges):
            ans[a] += i
        b = 0
        max_edge = float(-inf)
        for i, a in enumerate(ans):
            if a > max_edge:
                b = i
                max_edge = a
        return b
