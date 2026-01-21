class Solution:
    def __init__(self):
        self.t=[-1 for i in range(101)]
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums,len(nums)-1)
        
    def solve(self,nums,i):
        if i==0 :
            return nums[i]
        if i<0:
            return 0
        if self.t[i]!=-1:
            return self.t[i]
        ch=nums[i]+self.solve(nums,i-2)
        ch2=self.solve(nums,i-1)
        self.t[i]=max(ch,ch2)
        return self.t[i]
    # def solve(self,nums,i):
    #     if i==0 :
    #         return nums[i]
    #     if i<0:
    #         return 0
        
       
    #     ch=nums[i]+self.solve(nums,i-2)
    #     ch2=self.solve(nums,i-1)
    #     return max(ch,ch2)