class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        V=n
        adjList=[[]for i in range(V)]
        for u,v,d in edges:
            adjList[u].append((v,d))
            adjList[v].append((u,d*2))
                
        pq = []                    
        dist=[float('inf')]*V
        dist[0]=0
        heapq.heappush(pq, (0,0)) 
        while pq:
            d, node = heapq.heappop(pq) 
            if d != dist[node]:
                continue
            for u,dis in adjList[node]:
                if dist[u]>dis+dist[node]:
                    dist[u]=dis+dist[node]
                    heapq.heappush(pq,(dist[u],u))
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist[n-1]   