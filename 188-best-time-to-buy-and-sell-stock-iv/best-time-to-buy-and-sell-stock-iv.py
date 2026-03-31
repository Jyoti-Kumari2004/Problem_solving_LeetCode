class Solution:
    def maxProfit(self, ki: int, prices: List[int]) -> int:
        # t=[[[-1]*3 for _ in range(2)] for i in range(1000001)]
        # return self.solve(prices,0,1,0,t)
        n=len(prices)
        t=[[[0]*(ki+2) for _ in range(2)] for _ in range(n+1)]
        m=2
        for i in range(n-1,-1,-1):
            for j in range(m):
                for k in range(ki+1):
                    if j==1:
                        t[i][j][k]=max(-prices[i]+t[i+1][0][k+1],t[i+1][1][k])
                    else:
                        t[i][j][k]=max(prices[i]+t[i+1][1][k],t[i+1][0][k])
        return t[0][1][0]
        
    def solve(self,prices,ind,buy,k,t):
        if ind>=len(prices):
            return 0
        if k>2:
            return 0
        if t[ind][buy][k]!=-1:
            return t[ind][buy][k]
        if buy:
            ch1=prices[ind]+self.solve(prices,ind+1,0,k+1,t)
            ch2=self.solve(prices,ind+1,1,k,t)
            t[ind][buy][k]=max(ch1,ch2)
            return max(ch1,ch2)
        else:
            ch1=-prices[ind]+self.solve(prices,ind+1,1,k,t)
            ch2=self.solve(prices,ind+1,0,k,t)
            t[ind][buy][k]=max(ch1,ch2)
            return max(ch1,ch2)
        
