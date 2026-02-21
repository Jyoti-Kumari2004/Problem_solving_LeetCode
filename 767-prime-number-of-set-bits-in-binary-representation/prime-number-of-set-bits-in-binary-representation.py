class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            if self.isPrime(self.setBits(i)):
                count+=1
        return count
    def setBits(self,n):
        count=0
        while n:
            if n&1==1:
                count+=1
            n=n>>1
        return count
    def isPrime(self,n):
        if n==2:
            return True
        if n%2==0:
            return False
        if n==0 or n==1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True
        