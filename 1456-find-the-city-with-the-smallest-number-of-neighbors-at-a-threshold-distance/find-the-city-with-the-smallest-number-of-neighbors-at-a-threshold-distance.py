class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf=float('inf')
        dist=[[inf]*n for i in range(n)]
        print(dist)
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][j]=0
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via]!=inf and dist[via][j]!=inf:
                        dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
        print(dist)
        curr_min=float('inf')
        ans=0
        
        for i in range(len(dist)):
            count=0
            for j in range(len(dist[0])):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1

            if curr_min>=count:
                ans=i
                curr_min=count
        return ans
        