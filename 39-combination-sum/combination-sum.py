class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        self.solve(0,candidates,0,[],target,res)
        return res
        
    def solve(self,ind,arr,summ,path,target,res):
        if summ>target or ind==len(arr):
            return 
        if summ==target:
            res.append(path.copy())
            return 
        path.append(arr[ind])
        summ+=arr[ind]
        self.solve(ind,arr,summ,path,target,res)
        path.pop()
        summ-=arr[ind]
        for i in range(ind+1,len(arr)) :
            summ+=arr[i]
            path.append(arr[i])
            self.solve(i,arr,summ,path,target,res)
            summ-=arr[i]
            path.pop()
        
        
        

        