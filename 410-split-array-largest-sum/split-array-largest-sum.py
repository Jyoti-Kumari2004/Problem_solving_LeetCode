class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k==1:
            return sum(nums)
        s=max(nums)
        e=sum(nums)
        ans=0
        while s<=e:
            mid=s+(e-s)//2
            if self.solve(nums,mid,k)==True:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
        
    def solve(self,nums,n,k):
        count=1
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s>n:
                count+=1
                s=nums[i]
            if count>k:
                return False
        return True
    

        


        