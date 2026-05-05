class Solution:
    def __init__(self):
        self.dir=[[1,0],[0,1],[-1,0],[0,-1]]
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        vis=[[False]*len(maze[0]) for i in range(len(maze))]
        vis[entrance[0]][entrance[1]]=True
        q=deque()
        q.append([entrance[0],entrance[1],0])
        ans=float('inf')
        n=len(maze)
        m=len(maze[0])
        while q:
            i,j,st=q.popleft()
            if (i == 0 or j == 0 or i == n-1 or j == m-1) and (i,j)!=(entrance[0],entrance[1]):
                ans=min(ans,st)
            for x,y in self.dir:
                nx=x+i
                ny=y+j
                if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]=="." and vis[nx][ny]==False:
                    vis[nx][ny]=True
                    q.append([nx,ny,st+1])
        if ans==float('inf'):
            return -1
        return ans
        
