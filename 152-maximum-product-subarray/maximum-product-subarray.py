class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pp=1
        sp=1
        maxi=float('-inf')
        flag=False
        for i in range(len(nums)):
            if nums[i]==0:
                pp=1
                flag=True
            else:
                pp*=nums[i]
                maxi=max(maxi,pp)
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==0:
                sp=1
                flag=True
            else:
                sp*=nums[j]
                maxi=max(maxi,sp)
        if maxi<0 and flag==True:
            return 0
        return maxi
