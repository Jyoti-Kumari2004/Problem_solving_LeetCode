class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2+str1!=str1+str2:
            return ""
        else:
            x=self.gcd(len(str1),len(str2))
            print(x)
            return str2[:x]
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a