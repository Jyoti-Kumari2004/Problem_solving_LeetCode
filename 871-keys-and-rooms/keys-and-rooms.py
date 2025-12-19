class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj=rooms
        visited=[False]*(len(rooms))
        visited[0]=True
        for i in visited:
            if i==False:
                self.dfs(visited,adj,i)
        print(visited)
        for i in visited: 
            if i==False: 
                return False 
        return True
    def dfs(self,visited,adj,s):
        visited[s]=True
        for u in adj[s]:
            if visited[u]==False:
                self.dfs(visited,adj,u)
        
        