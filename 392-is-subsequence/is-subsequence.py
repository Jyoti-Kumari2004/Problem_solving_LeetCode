class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # return self.solve(len(s),len(t),s,t)
        i=len(s)-1
        j=len(t)-1
        if not s and not t:
            return True
        if len(s)>len(t):
            return False
        while i>=0 and j>=0:
            if s[i]==t[j]:
                i-=1
                j-=1
            else:
                j-=1
        if i>j:
            return False
        print(i,j)
        return True

    def solve(self,i,j,s,t):
        if i==0:
            return True
        if j==0:
            return False
        if s[i-1]==t[j-1]:
            return self.solve(i-1,j-1,s,t)
        else:
            return self.solve(i,j-1,s,t)
        
            
            
        