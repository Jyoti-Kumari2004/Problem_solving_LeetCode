class Solution:
    def __init__(self):
        self.t=[[-1]*101 for i in range(101)]
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m,n)
    def solve(self,m,n):
        t=[[None]*n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    t[i][j]=1
        for i in range(1,m):
            for j in range(1,n):
                t[i][j]=t[i][j-1]+t[i-1][j]
        
        return t[m-1][n-1]
   
    #memoization
    # def solve(self,i,j,m,n):
    #     if i==m-1 and j==n-1:
    #         return 1
    #     if i>m or j>n:
    #         return 0
    #     if self.t[i][j]!=-1:
    #         return self.t[i][j]
    #     r=self.solve(i,j+1,m,n)
    #     d=self.solve(i+1,j,m,n)
    #     self.t[i][j]=r+d
    #     return r+d

    
    #bottum-up recurrsion
    # def solve(self,i,j):
    #     if i==0 and j==0:
    #         return 1
    #     if i<0 or j<0:
    #         return 0
    #     r=self.solve(i,j-1)
    #     d=self.solve(i
    # -1,j)
    #     return r+d
    #top-down recurrsion
    # def solve(self,i,j,m,n):
    #     if i==m-1 and j==n-1:
    #         return 1
    #     if i>m or j>n:
    #         return 0
    #     r=self.solve(i,j+1,m,n)
    #     d=self.solve(i+1,j,m,n)

    #     return r+d

        