class Solution:
    def minFlips(self, s: str) -> int:
        x=self.solve(s+s,len(s),"0")
        y=self.solve(s+s,len(s),"1")
        return min(x,y)
    
    def solve(self,s,k,ch):
        i=0
        j=0
        count=0
        ch1=ch
        if ch=="0":
            ch2="1"
        else:
            ch2="0"
        ans=float('inf')
        while j<len(s):
            if j%2==0 and s[j]!=ch1:
                count+=1
            elif j%2!=0 and s[j]!=ch2:
                count+=1
            if k<j-i+1:
                if i%2==0 and s[i]!=ch1:
                    count-=1
                elif i%2!=0 and s[i]!=ch2:
                    count-=1
                i+=1
            if k==j-i+1:
                ans=min(ans,count)
            j+=1
        return ans



    


        