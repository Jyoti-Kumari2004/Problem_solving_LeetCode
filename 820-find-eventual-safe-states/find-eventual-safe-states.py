class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        indegree=[0]*V
        adjList=[[]for _ in range(V)]
        for i in range(V):
            for j in graph[i]:
                adjList[j].append(i)
                indegree[i]+=1 
        print(adjList)
        print(indegree)
        
        res=[]
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            res.append(node)
            for u in adjList[node]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
        res.sort()
        return res