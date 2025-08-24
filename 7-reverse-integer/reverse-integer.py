class Solution:
    def reverse(self, x: int) -> int:
        a=0
        res=0
        n=x
        x=abs(x)
        while x!=0:

            a=x%10
            res=a+(res*10)
            x=x//10
        if res>(2**31 - 1):
            return 0
        elif n<0:
            return -res
        return res