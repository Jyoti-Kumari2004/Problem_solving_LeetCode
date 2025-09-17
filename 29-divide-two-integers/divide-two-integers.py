class Solution:
    
    def divide(self, dividend: int, divisor: int) -> int:
        s=0
        ans=0
        a=abs(divisor)
        e=abs(dividend)
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        while s<=e:
            mid=(s+e)//2
            if (mid*a<=abs(dividend)):
                ans=mid
                s=mid+1                
            else:
                e=mid-1
        if divisor<0 and dividend<0:
            return ans
        elif divisor<0 or dividend<0:
            return -ans
        else:
            return ans