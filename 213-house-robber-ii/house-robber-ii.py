class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        return max(self.solve(nums[1:]),self.solve(nums[:n-1]))
    def solve(self,nums):
        if len(nums)==0:
            return 0
        prev2=0
        prev1=nums[0]
        for i in range(1,len(nums)):
            ch=nums[i]+(prev2 if i>1  else 0)
            ch2=prev1
            curr=max(ch,ch2)
            prev2,prev1=prev1,curr
        return prev1
            
    