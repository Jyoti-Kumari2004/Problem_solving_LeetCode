class Solution:
    def __init__(self):
        self.count=0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        s=set()
        for x,y in connections:
            s.add((x,y))
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        print(adj,s)
        vis=[False]*n
        for i in range(n):
            if vis[i]==False:
                self.solve(i,vis,adj,s)
        return self.count
    def solve(self,src,vis,adj,s):
        vis[src]=True
        for u in adj[src]:
            if vis[u]==False:
                if (src,u) in s:
                    self.count+=1
                self.solve(u,vis,adj,s)
        


        