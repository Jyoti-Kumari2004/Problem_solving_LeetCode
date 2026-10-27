class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        vis=set()
        count=0
        self.dir=[[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and (i,j) not in vis:
                    s=[grid[i][j]]
                    self.dfs(i,j,vis,grid,s)
                    if s[0]%k==0:
                        count+=1
        return count
    def dfs(self,i,j,vis,grid,s):
        vis.add((i,j))
        for x,y in self.dir:
            nx=x+i
            ny=y+j
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in vis and grid[nx][ny]!=0:
                s[0]+=grid[nx][ny]
                self.dfs(nx,ny,vis,grid,s)



        