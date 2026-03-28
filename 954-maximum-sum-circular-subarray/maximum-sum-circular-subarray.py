class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        x1=nums[0]
        ans=float('-inf')
        ans2=float('inf')
        for i in range(1,len(nums)):
            x1=max(x1+nums[i],nums[i])
            ans=max(ans,x1)
        x2=nums[0]
        for i in range(1,len(nums)):
            x2=min(x2+nums[i],nums[i])
            ans2=min(x2,ans2)
        if sum(nums)==ans2:
            return ans
        return max(ans,sum(nums)-ans2)
        