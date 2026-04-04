class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        ans=0
        s=0
        e=x//2
        while s<=e:
            mid=s+(e-s)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans