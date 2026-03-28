class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        vis=[False]*(n*n)
        x=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[grid[i][j]-1]==True:
                    x=grid[i][j]
                vis[grid[i][j]-1]=True
        y=0
        for i in range(len(vis)):
            if vis[i]==False:
                y=i+1
        return [x,y]
        

        