class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=sorted(arr,key=lambda x:(bin(x).count("1"),x))
        return res
    def countSetBits(self,n):
        count=0
        while n:
            if n&1==1:
                count+=1
            n=n>>1
        return count
        