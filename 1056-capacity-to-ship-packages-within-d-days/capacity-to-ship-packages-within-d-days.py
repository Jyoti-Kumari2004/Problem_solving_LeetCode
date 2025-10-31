class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s=max(weights)
        e=sum(weights)
        ans=0
        while s<=e:
            mid=s+(e-s)//2
            if self.isvalid(mid,weights,days)==True:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
    def isvalid(self,mid,weights,days):
        count=1
        s=0
        for i in range(len(weights)):
            s+=weights[i]
            if s>mid:
                count+=1
                s=weights[i]
        if count<=days:
            return True
        else:
            return False
            
        