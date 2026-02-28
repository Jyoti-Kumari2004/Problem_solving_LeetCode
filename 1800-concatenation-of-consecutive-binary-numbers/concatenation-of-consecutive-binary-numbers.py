class Solution:
    def concatenatedBinary(self, n: int) -> int:
        fin=""
        for i in range(1,n+1):
            ad=bin(i)
            ad=ad[2:]
            fin+=ad
        ans=int(fin,2)%1000000007
        return ans