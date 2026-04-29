class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        s=0
        ans=float('-inf')
        while j<len(nums):
            s+=nums[j]
            if j-i+1>k:
                s-=nums[i]
                i+=1
            if j-i+1==k:
                avg=s/k
                ans=max(ans,avg)
            j+=1
        return ans
        