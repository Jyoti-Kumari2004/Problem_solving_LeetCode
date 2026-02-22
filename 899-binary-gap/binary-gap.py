class Solution:
    def binaryGap(self, n: int) -> int:
        s=bin(n)
        s=s[2:]
        print(s)
        if self.setbit(n)<=1 :
            return 0
        
        ct=0
        i=0
        ans=0
        while s[i]!="1":
            i+=1
        while i<len(s):
            if s[i]=="1":
                ans=max(ct+1,ans)
                ct=0
            else:
                ct+=1
            i+=1
        return ans



    def setbit(self,n):
        count=0
        while n:
            if n&1==1:
                count+=1
            n=n>>1
        return count
        