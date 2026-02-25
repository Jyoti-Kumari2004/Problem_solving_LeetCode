class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n:
            return []
        res=[]
        self.solve(1,n,[],res,k,n,0)
        return res
    
    def solve(self,ind,n,path,res,k,target,curr_sum):
        if curr_sum>target:
            return

        if len(path)==k and curr_sum==target:
            res.append(path.copy())
        for i in range(ind,10):
            path.append(i)
            curr_sum+=i
            self.solve(i+1,n,path,res,k,target,curr_sum)
            path.pop()
            curr_sum-=i
        