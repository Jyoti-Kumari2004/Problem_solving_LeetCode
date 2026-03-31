class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        # return self.solve(0,prices,0)
        n=len(prices)
        m=2
        t=[[0]*2 for i in range(n+3)]
        t[n][0]=0
        t[n][1]=0
        for i in range(n-1,-1,-1):
            for j in range(m):
                if j==1:
                    t[i][j]=max(prices[i]+t[i+2][0],t[i+1][1])
                else:
                    t[i][j]=max(-prices[i]+t[i+1][1],t[i+1][0])
        print(t)
        return t[0][0]
    
    def solve(self,ind,prices,buy):
        if ind>=len(prices):
            return 0
        if buy:
            ch1=prices[ind]+self.solve(ind+2,prices,0)
            ch2=self.solve(ind+1,prices,1)
            return max(ch1,ch2)
        else:
            ch1=-prices[ind]+self.solve(ind+1,prices,1)
            ch2=self.solve(ind+1,prices,0)
            return max(ch1,ch2)


        