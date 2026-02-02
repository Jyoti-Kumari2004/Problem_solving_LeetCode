class Solution:
    def __init__(self):
        self.t=[[-1]*2 for i in range(30001)]
    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices,0,1)

    def solve(self,prices,i,buy):
        if i>=len(prices):
            return 0
        if self.t[i][buy]!=-1:
            return self.t[i][buy]
        if buy:
            ch1=-prices[i]+self.solve(prices,i+1,0)
            ch2=0+self.solve(prices,i+1,1)
            self.t[i][buy]=max(ch1,ch2)
            return max(ch1,ch2)
        else:
            ch3=prices[i]+self.solve(prices,i+1,1)
            ch4=0+self.solve(prices,i+1,0)
            self.t[i][buy]=max(ch3,ch4)
            return max(ch3,ch4)
    #recurrsive code
    # def solve(self,prices,i,buy):
    #     if i>=len(prices):
    #         return 0
        
    #     if buy:
    #         ch1=-prices[i]+self.solve(prices,i+1,0)
    #         ch2=0+self.solve(prices,i+1,1)
    #         return max(ch1,ch2)
    #     else:
    #         ch3=prices[i]+self.solve(prices,i+1,1)
    #         ch4=0+self.solve(prices,i+1,0)
    #         return max(ch3,ch4)
        