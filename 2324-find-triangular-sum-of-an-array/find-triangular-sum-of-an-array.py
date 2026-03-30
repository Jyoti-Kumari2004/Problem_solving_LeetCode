class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        up=nums
        n=len(nums)
        while n-1>0:
            for i in range(len(nums)-1):
                nums[i]=(nums[i+1]+nums[i])%10
            n-=1
        return nums[0]
        