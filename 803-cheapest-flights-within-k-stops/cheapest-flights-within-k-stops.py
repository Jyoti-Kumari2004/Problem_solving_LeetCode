class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList=[[]for i in range(n)]
        for u,v,dist in flights:
            adjList[u].append([v,dist])
        # print(adjList)
        dist=[float('inf')]*n
        q=deque()
        q.append((0,src,0))
        while q:
            stops,node,d=q.popleft()
            if stops>k: continue
            for v, di in adjList[node] :
                if dist[v]>d+di and stops<=k:
                    dist[v]=d+di
                    q.append((stops+1,v,dist[v]))
            
        if dist[dst]==float('inf'):return -1
        return dist[dst]
            


        