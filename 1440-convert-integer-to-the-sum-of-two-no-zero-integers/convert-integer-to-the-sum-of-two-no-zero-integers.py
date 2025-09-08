class Solution:
    def checkZero(self,num):
        while(num>0):
            if num%10==0:
                return False
            num=num//10
        return True
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            a=i
            b=n-i
            if self.checkZero(a) and self.checkZero(b):
                return [a,b]