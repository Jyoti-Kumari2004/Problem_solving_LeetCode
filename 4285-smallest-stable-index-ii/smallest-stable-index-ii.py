class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int: 
        mini=[0]*len(nums)
        mini[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            mini[i]=min(nums[i],mini[i+1])
        print(mini)
        maxi=float('-inf')
        ans=float('inf')
        ans_i=0
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            if maxi-mini[i]<=k:
                return i
        
        return -1
        