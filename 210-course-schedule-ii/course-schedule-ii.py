class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        V=numCourses
        
        adjList=[[]for _ in range(V)]
        for u,v in prerequisites:
            adjList[u].append(v)
        indegree=[0]*V
        for i in range(len(adjList)):
            for j in adjList[i]:
               indegree[j]+=1
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
        if len(res)!=V:
            return []
        
        return res[::-1]