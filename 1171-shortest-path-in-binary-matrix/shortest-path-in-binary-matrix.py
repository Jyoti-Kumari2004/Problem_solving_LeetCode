class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1

        n=len(grid)
        m=len(grid[0])

        dist=[[float('inf') for i in range(m)]for i in range(n)]
        dist[0][0]=1

        q=deque()
        q.append((1,0,0))
        dir=[(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)]
        while q:
            d,i,j=q.popleft()
            for x,y in dir:
                ni=x+i
                nj=y+j
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]==0 :
                    if dist[ni][nj]>d+1:
                        dist[ni][nj]=d+1
                        q.append((dist[ni][nj],ni,nj))
                        
        for i in range(n):
            for j in range(m):
                if dist[i][j]==float('inf'):
                    dist[i][j]=-1
        print(dist)
        return dist[n-1][m-1]

        
























        # if not edges:
        #     return -1
        # V=n
        # adjList=[[]for i in range(V)]
        # for u,v,d in edges:
        #     u-=1
        #     v-=1
        #     adjList[u].append((v,d))
        #     adjList[v].append((u,d))
        
        
        # pq = []
        # parent=[-1]*V
        # dist=[float('inf')]*V
        # dist[0]=0
        # heapq.heappush(pq, (0, 0)) 
        # while pq:
        #     d, node = heapq.heappop(pq) 
        #     if d != dist[node]:
        #         continue
        #     for u,dis in adjList[node]:
        #         if dist[u]>dis+dist[node]:
        #             dist[u]=dis+dist[node]
        #             heapq.heappush(pq,(dist[u],u))
        #             parent[u]=node
        # if dist[-1]==float('inf'):
        #     return [-1]
        
        
        # path=[]
        # curr=n-1
        # while curr!=-1:
        #     path.append(curr+1)
        #     curr=parent[curr]
        # return [dist[-1]]+path
            
            
        