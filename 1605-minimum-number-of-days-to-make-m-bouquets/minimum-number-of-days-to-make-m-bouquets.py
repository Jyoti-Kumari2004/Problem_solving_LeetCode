class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        s=0
        e=max(bloomDay)
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if self.check(mid,bloomDay,k,m)==True:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
    def check(self,n,nums,k,m):
        ct=0
        gp=0
        for i in range(len(nums)):
            if nums[i]<=n:
                ct+=1
                if ct==k:
                    gp+=1
                    ct=0
            else:
                ct=0
        if gp>=m:
            return True
        return False