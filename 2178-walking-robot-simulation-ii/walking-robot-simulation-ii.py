class Robot:

    def __init__(self, width: int, height: int):
        self.w=width
        self.h=height
        self.perimeter = 2 * (self.w - 1 + self.h - 1)
        self.curr_i=0
        self.curr_j=0
        self.curr_dir=0
        self.dir=[(1,0), (0,1), (-1,0), (0,-1)]  # E, N, W, S
        self.value = {0:"East", 1:"North", 2:"West", 3:"South"}
        

    def step(self, num: int) -> None:
        num=num%self.perimeter
        if num==0:
            num=self.perimeter
        i=0
        move=0
        while i<num:
            x,y=self.dir[self.curr_dir]
            if 0<=self.curr_i+x<self.w and 0<=self.curr_j+y<self.h:
                self.curr_i+=x
                self.curr_j+=y
                i+=1
                move=0
            else:
                self.curr_dir=(self.curr_dir+1)%4
                move+=1
                if move==4:
                    break

        

    def getPos(self) -> List[int]:
        return [self.curr_i,self.curr_j]
        

    def getDir(self) -> str:
        return self.value[self.curr_dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()