class Solution:
    def numSub(self, s: str) -> int:
        i=0
        j=0
        ans=0
        while j<len(s):
            if s[j]=='0':
                ans+=self.summ(j-i)
                i=j+1
                
            j+=1
        ans+=self.summ(j-i)

        return ans%(1000000007)

    def summ(self,n):
        return (n*(n+1))//2
        