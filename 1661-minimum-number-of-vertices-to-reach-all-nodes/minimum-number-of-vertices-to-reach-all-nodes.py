class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        V=n
        indeg=[0]*V
        for u,v in edges:
            indeg[v]+=1
        ans=[]
        for i in range(len(indeg)):
            if indeg[i]==0:
                ans.append(i)
        return ans
        
         
        
