class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        for i in range(len(graph)):
            if color[i]==-1:
                if self.dfs(graph,color,i,0)==False:
                    return False
        return True


    def dfs(self,adjList,color,s,rang):
        color[s]=rang
        for u in adjList[s]:
            if color[u]==-1:
                if self.dfs(adjList,color,u,1-rang)==False:
                    return False
            elif color[u]==rang:
                return False
            
        return True
        

        