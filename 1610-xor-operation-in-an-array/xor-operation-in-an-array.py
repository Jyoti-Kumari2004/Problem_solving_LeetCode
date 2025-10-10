class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s=start
        res=0
        for i in range(n):
            num=start+2*i
            res=res^num
        return res


        