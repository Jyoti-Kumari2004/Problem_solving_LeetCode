class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        self.solve(n,0,0,k,[],res)
        return res

    def solve(self,n,ind,curr_k,k,path,res):
        
        if k==curr_k:
            res.append(path.copy())
            return 
        for i in range(ind+1,n+1):
            path.append(i)
            curr_k+=1
            self.solve(n,i,curr_k,k,path,res)
            curr_k-=1
            path.pop()
        