class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        t=0
        q=deque()
        fresh_count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh_count+=1
        
        dir=[[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            i,j,t=q.popleft()
            for x,y in dir:
                nr=i+x
                nc=j+y
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                    q.append((nr,nc,t+1))
                    grid[nr][nc]=2
                    fresh_count-=1
        return t if fresh_count==0 else -1
                


        