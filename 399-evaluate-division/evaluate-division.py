class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        i=0
        adj=defaultdict(list)
        for u,v in equations:
            adj[u].append((v,values[i]))
            adj[v].append((u,1/values[i]))
            i+=1
        ans=[]
        for n1,n2 in queries:
            if n1 not in adj.keys() or n2 not in adj.keys():
                val=-1
            elif n1==n2:
                val=1
            else:
                val=self.bfs(adj,n1,n2)
            ans.append(val)
        return ans
    def bfs(self,adj,n1,n2):
        vis={}
        for key,value in adj.items():
            vis[key]=False
        q=deque()
        q.append([n1,1])
        while q:
            node,m=q.popleft()
            if node==n2:
                return m
            for u,mul in adj[node]:
                if vis[u]==False:
                    q.append([u,mul*m])
                    vis[u]=True
        return -1
        
    
        

        