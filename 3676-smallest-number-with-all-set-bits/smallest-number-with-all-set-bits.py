class Solution:
    def smallestNumber(self, n: int) -> int:
        a=""
        a+=(bin(n))
        a=a.replace("0b", "")
        print(a)
        b=""
        for i in range(len(a)):
            b+=("1")
        print(b)
        return int(b,2)
        