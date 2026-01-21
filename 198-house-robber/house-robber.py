class Solution:
    
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums)
    # below code is top-down dp approach
    def solve(self,nums):
        prev2=0
        prev1=nums[0]
        for i in range(1,len(nums)):
            ch=nums[i]+(prev2 if i>1  else 0)
            ch2=prev1
            curr=max(ch,ch2)
            prev2=prev1
            prev1=curr
        return prev1

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