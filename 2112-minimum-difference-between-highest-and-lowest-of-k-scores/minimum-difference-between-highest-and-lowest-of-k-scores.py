class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float('inf')
        i=0
        j=0
        while j<len(nums):
            if j-i+1>k:
                i+=1
            if k==j-i+1:
                ans=min(ans,nums[j]-nums[i])
            j+=1
        return ans

                