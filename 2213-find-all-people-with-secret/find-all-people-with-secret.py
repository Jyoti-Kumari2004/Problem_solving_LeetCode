class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        #making batch according to time 
        visited=[False]*n
        visited[0]=True
        visited[firstPerson]=True
        i=0
        while i<len(meetings):
            adj=defaultdict(list)
            j=meetings[i][2]
            parti=set()
            temp_visited=[False]*n
            while i<len(meetings) and j==meetings[i][2]:
                u=meetings[i][0]
                v=meetings[i][1]
                adj[u].append(v)
                adj[v].append(u)
                parti.add(u)
                parti.add(v)
                i+=1
            for p in parti:
                if visited[p]==True:
                    temp_visited[p]=True
            for p in parti:
                if temp_visited[p]==True: 
                    self.dfs(temp_visited,adj,p)
            for p in parti:
                if temp_visited[p]==True:
                    visited[p]=True

        print(visited)
        ans=[]
        for v in range(len(visited)):
            if visited[v]==True:
                ans.append(v)
        return ans


            





        # in the second solution i given..tle comes because of the temp visited....i need to make temp visited ..nhi to for large data its time taking to evaluated all the nodes

    #     visited=[False]*n
    #     visited[0]=True
    #     visited[firstPerson]=True
    #     adj=[[]for i in range(n)]
    #     for u,v,t in meetings:
    #         if visited[u]==True or visited[v]==True:
    #             adj[u].append(v)
    #             adj[v].append(u)
    #             if visited[u]==True:
    #                 self.dfs(visited,adj,u)
    #             else:
    #                 self.dfs(visited,adj,v)
    #     print(visited)
    #     print(adj)
    #     ans=[]
    #     for i in range(len(visited)):
    #         if visited[i]==True:
    #             ans.append(i)
    #     return ans
    def dfs(self,visited,adj,s):
        visited[s]=True
        for u in adj[s]:
            if visited[u]==False:
                self.dfs(visited,adj,u)
        


               




        