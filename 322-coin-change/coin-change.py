class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)+1
        m=amount+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if j==0:
                    t[i][j]=0
                if i==0:
                    t[i][j]=float('inf')
        for j in range(1,m):
            if j%coins[0]==0:
                t[1][j]=j//coins[0]
            else:
                t[1][j]=float('inf')
        for i in range(2,n):
            for j in range(1,m):
                if coins[i-1]<=j:
                    t[i][j]=min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        if t[n-1][m-1]==float('inf'):
            return -1
        return t[n-1][m-1]
                
        