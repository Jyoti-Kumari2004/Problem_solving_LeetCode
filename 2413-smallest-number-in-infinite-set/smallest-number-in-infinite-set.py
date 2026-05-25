class SmallestInfiniteSet:

    def __init__(self):
        self.q=[]
        self.curr=1
        self.s=set()
        

    def popSmallest(self) -> int:
        if self.q and self.q[0]<self.curr:
            ele=heapq.heappop(self.q)
            self.s.remove(ele)
            return ele
        else:
            val=self.curr
            self.curr+=1
            return val

    def addBack(self, num: int) -> None:
        if num<self.curr and num not in self.s:
            heapq.heappush(self.q,num)
            self.s.add(num)


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)