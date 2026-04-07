class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.d = 0
        self.dir = {'East': [1,0], 'North': [0,1], 'West': [-1,0], 'South':[0,-1]}
        self.x = 0
        self.y = 0
        self.per = 2 * (self.w + self.h) - 4

    def step(self, num: int) -> None:
        if self.per == 0:
            return 
        num %= self.per
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.d = 3
            return 
        while num != 0:
            dx, dy = list(self.dir.values())[self.d]
            i = self.x + ( num * dx )
            j = self.y + ( num * dy )
            if i < 0 or i > ( self.w - 1 ) or j < 0 or j > ( self.h - 1):
                if i > self.w - 1:
                    self.x = self.w - 1
                    num = i - ( self.w - 1 )
                elif i < 0:
                    self.x = 0
                    num = (-1) * i
                elif j > self.h - 1:
                    self.y = self.h - 1
                    num = j - ( self.h - 1 )
                elif j < 0:
                    self.y = 0
                    num = (-1) * j
                self.d = (self.d + 1) % 4
            else:
                self.x = i
                self.y = j
                num = 0
                

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return list(self.dir.keys())[self.d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()