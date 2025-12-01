class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False for i in range(len(grid[0]))]for j in range(len(grid))]
        i,j=0,0
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j]==False:
                    count+=1
                    self.bfs(i,j,grid,visited)
                    
        return count





    def bfs(self,i,j,grid,visited):
        q=deque()
        q.append((i,j))
        visited[i][j]=True
        dir=[[0,-1],[0,1],[1,0],[-1,0]]
        while q:
            x,y=q.popleft()
            for a,b in dir:
                if 0<=x+a<len(grid) and 0<=y+b<len(grid[0]) and grid[x+a][y+b]=="1" and visited[x+a][y+b]==False:
                    visited[x+a][y+b]=True
                    q.append((x+a,y+b))

