class Solution:
    def maximumSwap(self, num: int) -> int:
        s=str(num)
        res=s
        for i in range(len(s)):
            maxi=max(s[i:])
            for j in range(i,len(s)):
                if s[j]==maxi and s[j]>s[i]:
                    s=self.swap(s,i,j)
                    res=max(s,res)
                    s=self.swap(s,i,j)
        return int(res)
    def swap(self,s,i,j):
        v=list(s)
        v[i],v[j]=v[j],v[i]
        return "".join(v)


            