class Solution:
    def __init__(self):
        self.t=[[-1]*10001 for i in range(101)]
    def superEggDrop(self, k: int, n: int) -> int:
        return self.solve(k,n)

    def solve(self,e,f):
        if f==0 or f==1:
            return f
        if e==1:
            return f
        if self.t[e][f]!=-1:
            return self.t[e][f]
        ans=float('inf')
        start,end=1,f
        while start<=end:
            k=start+(end-start)//2
            if self.t[e-1][k-1]!=-1:
                l=self.t[e-1][k-1]
            else:
                l=self.solve(e-1,k-1)
                self.t[e-1][k-1]=l
            if self.t[e][f-k]!=-1:
                r=self.t[e][f-k]
            else:
                r=self.solve(e,f-k)
                self.t[e][f-k]=r

            temp_ans=1+max(l,r)
            ans=min(ans,temp_ans)
            if l > r:
                end = k - 1
            else:
                start = k + 1
        self.t[e][f]=ans
        return ans
        