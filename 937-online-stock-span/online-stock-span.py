class StockSpanner:

    def __init__(self):
        self.arr=[]
        self.st=[]
        self.ind=-1
        

    def next(self, price: int) -> int:
        self.ind+=1
        self.arr.append(price)
        #optimized method: using monotonic stack
        while self.st and self.arr[self.st[-1]]<=price:
            self.st.pop()
        res = self.ind - self.st[-1]-1 if self.st else self.ind
        self.st.append(self.ind)
        return res+1






        #naive method
        # count=1
        # for i in range(len(self.arr)-2,-1,-1):
        #     if self.arr[i]>price:
        #         break
        #     else:
        #         count+=1
        # return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)