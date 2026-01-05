class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m=amount+1
        n=len(coins)+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
        for i in range(1,n):
            for j in range(1,m):
                if coins[i-1]<=j:
                    t[i][j]=t[i-1][j]+t[i][j-coins[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        return t[n-1][m-1]
