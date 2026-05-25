class MedianFinder:

    def __init__(self):
        self.l=[]
        self.r=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.l,-num)
        if self.r and self.l and -(self.l[0])>self.r[0]:
            ele=heapq.heappop(self.l)
            heapq.heappush(self.r,-ele)


        if len(self.l)-len(self.r)>1:
            ele=heapq.heappop(self.l)
            heapq.heappush(self.r,-ele)
        if len(self.r)-len(self.l)>1:
            ele=heapq.heappop(self.r)
            heapq.heappush(self.l,-ele)

        

    def findMedian(self) -> float:
        if len(self.l)==len(self.r):
            ele1=heapq.heappop(self.l)
            ele2=heapq.heappop(self.r)
            heapq.heappush(self.l,ele1)
            heapq.heappush(self.r,ele2)
            return ((-ele1)+ele2)/2
        elif len(self.l)>len(self.r):
            ele1=heapq.heappop(self.l)
            heapq.heappush(self.l,ele1)
            return -ele1
        else:
            ele2=heapq.heappop(self.r)
            heapq.heappush(self.r,ele2)
            return ele2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()