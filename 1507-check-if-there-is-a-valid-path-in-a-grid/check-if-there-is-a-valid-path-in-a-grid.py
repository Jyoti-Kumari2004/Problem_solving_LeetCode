class Solution:
    def __init__(self):
        self.d={1:[[0,1],[0,-1]],2:[[1,0],[-1,0]],3:[[0,-1],[1,0]],4:[[0,1],[1,0]],5:[[0,-1],[-1,0]],6:[[0,1],[-1,0]]}
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        return self.dfs(0,0,grid,n,m,vis)
    def dfs(self,i,j,grid,n,m,vis):
        vis[i][j]=True
        if i==n-1 and j==m-1:
            return True
        for x,y in self.d[grid[i][j]]: 
            nx=x+i
            ny=y+j
            rx = -x
            ry = -y
            if 0<=nx<n and 0<=ny<m and vis[nx][ny]==False and [rx,ry] in self.d[grid[nx][ny]]:
                if self.dfs(nx,ny,grid,n,m,vis):
                    return True
        return False

        