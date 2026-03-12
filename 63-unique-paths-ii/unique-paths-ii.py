class Solution:
    def __init__(self):
        self.t=[[-1]*101 for i in range(101)]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid)

    def solve(self,i,j,grid):
        if grid[i][j]==1:
            return 0
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if self.t[i][j]!=-1:
            return self.t[i][j]
        self.t[i][j]=self.solve(i-1,j,grid)+self.solve(i,j-1,grid)
        return self.t[i][j]
        