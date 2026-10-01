class Solution:
    def __init__(self):
        self.t={}
    def combinationSum4(self, nums: list[int], target: int) -> int:
        return self.solve(target,nums)
        
    def solve(self,target,nums):
        
        if target==0:
            return 1
        if target<0:
            return 0
        if target in self.t:
            return self.t[target]
        ans=0
        for num in nums:
            ans+=self.solve(target-num,nums)
        self.t[target]=ans
        return ans