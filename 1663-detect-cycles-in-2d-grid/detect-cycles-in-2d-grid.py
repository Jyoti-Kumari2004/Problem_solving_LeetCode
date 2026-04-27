class Solution:
    def __init__(self):
        self.dir=[[0,1],[1,0],[0,-1],[-1,0]]
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*len(grid[0]) for i in range(len(grid))]
        for i in range(n):
            for j in range(m):
                if vis[i][j]==False:
                    si=i
                    sj=j
                    if self.dfs(si,sj,i,j,1,grid,vis,grid[i][j]):
                        return True
        return False
    def dfs(self,pi,pj,i,j,path,grid,vis,ch):
        vis[i][j]=True
        for x,y in self.dir:
            nx=x+i
            ny=y+j
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==ch:
                if  vis[nx][ny]==False :
                    if self.dfs(i,j,nx,ny,path+1,grid,vis,ch)==True:
                        return True
                else:
                    if (nx,ny)!=(pi,pj):
                        return True
            


                    
        