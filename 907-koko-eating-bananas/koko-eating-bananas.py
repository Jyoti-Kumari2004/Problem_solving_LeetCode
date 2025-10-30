class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s=1
        e=max(piles)
        ans=0
        while s<=e:
            mid=s+(e-s)//2
            if self.isvalid(mid,piles,h)==True:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
    def isvalid(self,m,piles,gh):
        h=0
        for i in range(len(piles)):
            h+=piles[i]//m
            if piles[i]%m!=0:
                h+=1
        if gh>=h:
            return True
        else:
            return False
        

