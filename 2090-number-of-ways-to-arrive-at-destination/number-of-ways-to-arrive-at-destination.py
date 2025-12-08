class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        V=n
        adjList=[[]for i in range(V)]
        for u,v,d in roads:
            adjList[u].append((v,d))
            adjList[v].append((u,d))
        
        pq = []                   
        dist=[float('inf')]*V
        dist[0]=0
        sh_p=[0]*V
        sh_p[0]=1
        heapq.heappush(pq, (0, 0)) 
        while pq:
            d, node = heapq.heappop(pq) 
            if d != dist[node]:
                continue
            for u,dis in adjList[node]:
                if dist[u]>dis+dist[node]:
                    sh_p[u]=(sh_p[node])%1000000007
                    dist[u]=dis+dist[node]
                    heapq.heappush(pq,(dist[u],u))
                elif dist[u]==dis+dist[node]:
                    sh_p[u]=(sh_p[u]+sh_p[node])%1000000007
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        print(sh_p)
        return sh_p[-1]
        