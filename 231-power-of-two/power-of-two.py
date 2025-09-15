import math
class Solution:
    def countbits(self,n):
        count=0
        while n>0:
            n=n&(n-1)
            count+=1
        return count
    def isPowerOfTwo(self, n: int) -> bool:
        if self.countbits(n)!=1:
            return False
        return True