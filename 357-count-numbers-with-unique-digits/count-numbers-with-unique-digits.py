class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt=[0]
        s=set()
        self.solve(0,cnt,s,n)
        return cnt[0]+1
        
    def solve(self,ind,cnt,s,n):
        if ind==n:
            return 
        for i in range(10):
            if i==0 and ind==0:
                continue
            if i not in s:
                cnt[0]+=1
                s.add(i)
                self.solve(ind+1,cnt,s,n)
                s.remove(i)
                

