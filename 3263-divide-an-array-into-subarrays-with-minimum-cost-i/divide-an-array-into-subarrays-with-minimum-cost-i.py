class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums)==3:
            return sum(nums)
        
        ans=nums[0]
        arr=nums[1:]
        arr.sort()
        return ans+arr[0]+arr[1]