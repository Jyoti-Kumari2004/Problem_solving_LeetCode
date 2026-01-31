class Solution:
    def __init__(self):
        self.nc=0
        self.ed=0
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[]for i in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        count=0
        visited=[False]*n
        
        for i in range(n):
            self.nc=0
            self.ed=0
            if visited[i]==False:
                nodes=0
                self.dfs(adj,visited,i,self.nc,self.ed)
                self.ed=self.ed//2
                print(self.ed,self.nc)
                if self.ed==(self.nc*(self.nc-1))//2:
                    count+=1
        return count
    def dfs(self,adj,visited,src,nc,ed):
        visited[src]=True
        self.nc+=1
        self.ed+=len(adj[src])
        for u in adj[src]:
            if visited[u]==False:
                self.dfs(adj,visited,u,self.nc,self.ed)

    