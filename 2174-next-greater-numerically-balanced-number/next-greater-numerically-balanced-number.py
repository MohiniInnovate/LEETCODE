class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        '''for i in range(n+1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i'''
        i = n + 1
        while True:
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i
            i += 1
