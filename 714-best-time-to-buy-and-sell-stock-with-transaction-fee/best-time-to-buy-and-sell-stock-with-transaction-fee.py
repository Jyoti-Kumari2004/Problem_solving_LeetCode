class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
                    t[i][j]=max(prices[i]+t[i+1][0],t[i+1][1])
                else:
                    t[i][j]=max(-prices[i]+t[i+1][1]-fee,t[i+1][0])
        print(t)
        return t[0][0]