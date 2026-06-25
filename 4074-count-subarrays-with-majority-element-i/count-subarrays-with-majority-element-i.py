class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            tc=0
            for j in range(i,len(nums)):
                tc=tc+(1 if nums[j]==target else 0)
                if tc>(j-i+1)//2 :
                    c+=1
        return c
