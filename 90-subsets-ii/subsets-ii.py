class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        self.solve(0,nums,[],res)
        return res

    def solve(self,ind,nums,path,res):
        
        res.append(path.copy())
        for i in range(ind,len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.solve(i+1,nums,path,res)
            path.pop()
            

        