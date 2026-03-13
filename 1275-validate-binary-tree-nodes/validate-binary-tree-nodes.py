class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        lr = set(leftChild + rightChild)
        node = -1
        for i in range(n):
            if i not in lr:
                node = i
                break
        if node == -1:
            return False
        q = deque()
        q.append(node)
        visit = set()
        while q:
            a = q.popleft()
            if a in visit:
                return False
            visit.add(a)
            l = leftChild[a]
            if l != -1:
                q.append(l)
            r = rightChild[a]
            if r != -1:
                q.append(r)
        
        return True if len(visit) == n else False
        