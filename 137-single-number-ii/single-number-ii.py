class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #efficient approach
        if not nums:
            return []
        nums=sorted(nums)
        i=1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
            i=i+3
        return nums[len(nums)-1]














        # res=0
        # for i in range(32):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[j]&(1<<i)!=0:
        #             count+=1
        #     if count%3==1:
        #         res=res|(1<<i)
        # return res
