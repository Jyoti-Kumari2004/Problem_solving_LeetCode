class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjls=self.MtoL(isConnected)
        visited=[False]*len(adjls)
        count=0
        for i in range(len(adjls)):
            if visited[i]==False:
                count+=1
                self.dfs(adjls,i,visited)
        return count

    def dfs(self,adj,s,visited):
        visited[s]=True
        for i in adj[s]:
            if visited[i]==False:
                self.dfs(adj,i,visited)


    def MtoL(self,mat):
        adj=[[]for x in range(len(mat))]
        for i in range(len(mat)):
            for j in range(i):
                if mat[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj