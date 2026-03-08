class Solution:
    def __init__(self):
        self.dir=[[1,0],[-1,0],[0,1],[0,-1]]
    def numIslands(self, grid: List[List[str]]) -> int:
        q=[]
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==False:
                    count+=1
                    self.dfs(visited,grid,i,j)
        return count
        
    def dfs(self,visited,grid,i,j):
        visited[i][j]=True
        for n,m in self.dir:
            nx=n+i
            ny=m+j
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and visited[nx][ny]==False and grid[nx][ny]=="1":
                self.dfs(visited,grid,nx,ny)



        