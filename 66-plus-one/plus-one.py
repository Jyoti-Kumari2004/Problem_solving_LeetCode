class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = "".join(map(str, digits))
        ans=int(ans)
        ans+=1
        op=str(ans)
        res=[]
        for i in op:
            res.append(int(i))
        return res