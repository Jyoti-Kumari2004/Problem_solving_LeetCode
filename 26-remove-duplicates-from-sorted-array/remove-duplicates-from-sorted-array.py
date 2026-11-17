class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        prev=None
        i=0
        while i<len(nums):
            prev=nums[i]
            nums[k]=prev
            k+=1
            while prev!=None and i<len(nums) and prev==nums[i]:
                i+=1
        return k
            

