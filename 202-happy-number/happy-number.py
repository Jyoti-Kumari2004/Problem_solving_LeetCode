class Solution:
    def isHappy(self, n: int) -> bool:
        num=n
        if n==1 :
            print("here")
            return True
        d=set()
        while num not in d:
            d.add(num)
            num=self.calc(num)
            if num==1:
                return True
        return False
    def calc(self,n):

        summ=0
        while n:
            x=(n%10)
            summ+=x*x
            n=n//10

        return summ
        