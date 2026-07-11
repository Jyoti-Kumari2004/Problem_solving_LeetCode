class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        num=""
        for i in str(n):
            if i !="0":
                num+=i
            s+=int(i)
        if num=="":
            return 0
        return int(num)*s