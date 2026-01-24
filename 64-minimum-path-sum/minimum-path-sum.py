class Solution:
    # def __init__(self):
    #     self.t= [[-1]*201 for i in range(201)]
    def minPathSum(self, grid: List[List[int]]) -> int:
        # return self.solve(len(grid)-1,len(grid[0])-1,grid)
        n=len(grid)
        m=len(grid[0])
        t=[[None]*m for i in range(n)]
        curr_sum=0
        for i in range(n):
            curr_sum+=grid[i][0]
            t[i][0]=curr_sum
        curr_sum=0
        for j in range(m):
            curr_sum+=grid[0][j]
            t[0][j]=curr_sum
        for i in range(1,n):
            for j in range(1,m):
                t[i][j]=grid[i][j]+min(t[i-1][j],t[i][j-1])
        return t[n-1][m-1]
                







    #memoiation soution
    # def solve(self,i,j,grid):
    #     if i==0 and j==0:
    #         return grid[0][0]
    #     if i<0 or j<0:
    #         return float('inf')
    #     if self.t[i][j]!=-1:
    #         return self.t[i][j]
    #     l=grid[i][j]+self.solve(i,j-1,grid)
    #     u=grid[i][j]+self.solve(i-1,j,grid)
    #     self.t[i][j]=min(l,u)
    #     return self.t[i][j]

    #recurrsive solution
    # def solve(self,i,j,grid):
    #     if i==0 and j==0:
    #         return grid[0][0]
    #     if i<0 or j<0:
    #         return float('inf')
    #     l=grid[i][j]+self.solve(i,j-1,grid)
    #     u=grid[i][j]+self.solve(i-1,j,grid)
    #     return min(l,u)
        