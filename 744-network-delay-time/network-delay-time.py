class Solution:
    def networkDelayTime(self, edges: List[List[int]], n: int, k: int) -> int:
        V=n
        adjList=[[]for i in range(V+1)]
        for u,v,d in edges:
            adjList[u].append((v,d))
            
        
        pq = []
        dist=[float('inf')]*(V+1)
        dist[k]=0
        dist[0]=0
        heapq.heappush(pq, (0, k)) 
        while pq:
            d, node = heapq.heappop(pq) 
            if d != dist[node]:
                continue
            for u,dis in adjList[node]:
                if dist[u]>dis+dist[node]:
                    dist[u]=dis+dist[node]
                    heapq.heappush(pq,(dist[u],u))
        ans=max(dist)
        if ans==float('inf'):
            return -1
        return ans
            