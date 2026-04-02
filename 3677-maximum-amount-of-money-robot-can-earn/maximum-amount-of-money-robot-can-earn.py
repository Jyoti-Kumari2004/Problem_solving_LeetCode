class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # return self.solve(0,0,0,coins)
        n=len(coins)
        m=len(coins[0])
        t=[[[float('-inf')]*4 for i in range(m) ]for i in range(n)]
        t[n-1][m-1][0]=max(coins[n-1][m-1], 0)
        t[n-1][m-1][1]=max(coins[n-1][m-1], 0)
        t[n-1][m-1][2]=coins[n-1][m-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                for k in range(2,-1,-1):
                    if i == n-1 and j == m-1:
                        continue
                    if coins[i][j]>=0: 
                        r2 = coins[i][j]+t[i][j+1][k] if j+1 < m else float('-inf')
                        d2 = coins[i][j]+t[i+1][j][k] if i+1 < n else float('-inf')
                        t[i][j][k]=max(r2,d2)
                    else:
                        r=t[i][j+1][k+1]if j+1 < m else float('-inf')
                        d=t[i+1][j][k+1]if i+1 < n else float('-inf')
                        r2 = coins[i][j]+t[i][j+1][k]if j+1 < m else float('-inf')
                        d2 = coins[i][j]+t[i+1][j][k]if i+1 < n else float('-inf')
                        t[i][j][k]=max(r,d,r2,d2)
        return t[0][0][0]



    
    def solve(self,i,j,k,coins):
        if k>2:
            return float('-inf')
        if i==len(coins)-1 and j==len(coins[0])-1:
            if coins[i][j]<0 and k<2:
                return 0
            return coins[i][j]  
        if i>=len(coins) or j>=len(coins[0]):
            return float('-inf')
        if self.t[i][j][k]is not None:
            return self.t[i][j][k]
        if coins[i][j]>=0:
            r=coins[i][j]+self.solve(i,j+1,k,coins)
            d=coins[i][j]+self.solve(i+1,j,k,coins)
            res=max(r,d)
        else:
            r=self.solve(i,j+1,k+1,coins)
            d=self.solve(i+1,j,k+1,coins)
            r2 = coins[i][j]+self.solve(i, j+1, k, coins)
            d2 = coins[i][j]+self.solve(i+1, j, k, coins)
            res=max(r,d,r2,d2)
        self.t[i][j][k]=res
        return res
        
        