class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        v=[]
        for i in range(1,n+1):
            v.append(i)
        index=0
        ans=-1
        return self.solve(v,k,index)
        
    def solve(self,v,k,index):
        if len(v)==1:
            return v[0]
        index=(index+k-1)%len(v)
        v.pop(index)
        return self.solve(v,k,index)
        


        