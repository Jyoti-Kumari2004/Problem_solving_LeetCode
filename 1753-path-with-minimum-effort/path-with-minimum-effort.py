class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
       
        n=len(heights)
        m=len(heights[0])

        dist=[[float('inf') for i in range(m)]for i in range(n)]
        dist[0][0]=0

        # prev=heights[0][0]
        pq=[]
        dir=[[-1,0],[1,0],[0,-1],[0,1]]
        heapq.heappush(pq, (0, 0,0)) 
        while pq:
            d,i,j=heapq.heappop(pq)
            for x,y in dir:
                ni=x+i
                nj=y+j
                if 0<=ni<n and 0<=nj<m:
                    new_effort=max(dist[i][j],abs(heights[i][j]-heights[ni][nj]))
                    if dist[ni][nj]>new_effort:
                        dist[ni][nj]=new_effort
                        heapq.heappush(pq,(dist[ni][nj],ni,nj))
                        
        for i in range(n):
            for j in range(m):
                if dist[i][j]==float('inf'):
                    dist[i][j]=-1
        print(dist)
        return dist[n-1][m-1]
        