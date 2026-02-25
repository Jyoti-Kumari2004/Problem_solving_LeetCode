class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.solve(0,candidates,0,[],target,res)
        return res
        
    def solve(self,ind,arr,summ,path,target,res):
        
        if summ==target:
            res.append(path.copy())
            return 
        if summ>target or ind==len(arr):
            return 
        for i in range(ind,len(arr)) :
            if i >ind and arr[i] == arr[i-1]:
                continue            
            summ+=arr[i]
            path.append(arr[i])
            self.solve(i+1,arr,summ,path,target,res)
            summ-=arr[i]
            path.pop()

        