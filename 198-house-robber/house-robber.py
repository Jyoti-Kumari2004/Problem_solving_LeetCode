class Solution:
    def __init__(self):
        self.t=[-1 for i in range(101)]
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums)
    def solve(self,nums):
        t=[0]*len(nums)
        t[0]=nums[0]
        for i in range(1,len(nums)):
            ch=nums[i]+(t[i-2] if i>1  else 0)
            ch2=t[i-1]
            t[i]=max(ch,ch2)
        return t[len(nums)-1]

    #memoiation solution: 
    # def solve(self,nums,i):
    #     if i==0 :
    #         return nums[i]
    #     if i<0:
    #         return 0
    #     if self.t[i]!=-1:
    #         return self.t[i]
    #     ch=nums[i]+self.solve(nums,i-2)
    #     ch2=self.solve(nums,i-1)
    #     self.t[i]=max(ch,ch2)
    #     return self.t[i]

    #recurrsive solution:
    # def solve(self,nums,i):
    #     if i==0 :
    #         return nums[i]
    #     if i<0:
    #         return 0
        
       
    #     ch=nums[i]+self.solve(nums,i-2)
    #     ch2=self.solve(nums,i-1)
    #     return max(ch,ch2)