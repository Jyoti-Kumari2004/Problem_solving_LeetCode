class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        maxi=0
        zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
                zeros+=1
            while count>1:
                if nums[l]==0:
                    count-=1
                l+=1
            
            maxi=max(maxi,r-l)
        
        return maxi
            
        