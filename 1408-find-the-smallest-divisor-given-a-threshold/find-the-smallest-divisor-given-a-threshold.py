class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s=1
        e=max(nums)
        ans=e
        while s<=e:
            mid=s+(e-s)//2
            a=self.summ(nums,mid)
            if a<=threshold:
                ans=mid
                e=mid-1 
            else:
                s=mid+1
        return ans
    def summ(self,nums,m):
        s=0
        for i in range(len(nums)):
            s+=nums[i]//m
            if nums[i]%m!=0:
                s+=1
        return s

