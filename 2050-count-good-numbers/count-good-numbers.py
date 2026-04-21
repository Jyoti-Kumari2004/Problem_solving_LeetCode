class Solution:
    def __init__(self):
        self.MOD=1000000007
    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5
        if n%2==0:
            #if even
            num=n//2
            return (self.pow(5,num)*self.pow(4,num))%1000000007
        else:
            ev=(n+1)//2
            od=n//2
            return (self.pow(5,ev)*self.pow(4,od))%1000000007
    def pow(self,x,n):
        if n>=0:
            return self.powerp(x,n)
        else: 
            return self.powern(x,n)
    def powerp(self,x,n):
        if n==0:
            return 1
        half=self.powerp(x,n//2)
        if n%2==0:
            
            return (half*half)%self.MOD
        else:
            return (x*half*half)%self.MOD
            

    def powern(self,x,n):
        return 1/(self.powerp(x,-n))
        