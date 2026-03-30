class Solution:
    def __init__(self):
        self.dir=[(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1

        n=len(grid)
        m=len(grid[0])
        dist=[[float('inf') for i in range(m)]for _ in range(n)]
        dist[0][0]=1
        q=[]
        heapq.heappush(q,[1,0,0])
        while q:
            d,i,j=heapq.heappop(q)
            for x,y in self.dir:
                ni=i+x
                nj=j+y
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]==0:
                    if d+1<dist[ni][nj]:
                        dist[ni][nj]=d+1
                        heapq.heappush(q,[d+1,ni,nj])
        print(dist)
        if dist[n-1][m-1]==float('inf'):
            return -1
        return dist[n-1][m-1]


