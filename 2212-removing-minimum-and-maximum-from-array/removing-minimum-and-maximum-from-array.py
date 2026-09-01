class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi=float('inf')
        ma=float('-inf')
        n=len(nums)
        for i in range(len(nums)):
            if mi>nums[i]:
                mini=i
                mi=nums[i]
            if ma<nums[i]:
                maxi=i
                ma=nums[i]
        print(mi,mini)
        print(ma,maxi)
        #first case:
        a=max(mini,maxi)+1
        b=max(n-mini,n-maxi)
        c=mini+(n-maxi)+1
        d=maxi+(n-mini)+1
        return min(a,b,c,d)
        