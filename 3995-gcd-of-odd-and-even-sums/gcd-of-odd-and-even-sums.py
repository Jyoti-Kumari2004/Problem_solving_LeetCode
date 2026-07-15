class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
    #     ce=0
    #     ev=0
    #     od=0
    #     ods=1
    #     for i in range(n):
    #         ev+=(ce+2)
    #         ce=ce+2
    #         od+=(ods+2)
    #         ods=ods+2
    #     print(ev,od)
    #     return self.gcd(ev,od)   
    # def gcd(self,a,b):
    #     if a == 0:
    #         return b
    #     if b == 0:
    #         return a
    #     if a == b:
    #         return a
    #     if a > b:
    #         return gcd(a - b, b)
    #     return gcd(a, b - a)
        return n