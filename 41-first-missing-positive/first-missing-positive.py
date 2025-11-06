class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        
        
        i=0
        while i<len(nums):
            idx=i+1
            if nums[i]<len(nums) and nums[i]>0 and nums[i] !=nums[nums[i]-1]:  
                    self.swap(i,nums[i]-1,nums)       
            else:
                i+=1
        
        for i in range(len(nums)):
            if ((i+1)!=nums[i]):
                return i+1
        if not nums:
            return 1
        return nums[-1]+1

    def swap(self,a,b,arr):
        arr[a],arr[b]=arr[b],arr[a]
        return arr