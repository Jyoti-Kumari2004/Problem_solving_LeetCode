class Solution:
    def sortVowels(self, s: str) -> str:
        a=[]
        for i in s:
            if i in "aeiouAEIOU":
                a.append(i)
        a=sorted(a)
        t=""
        j=0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU" :
                t+=a[j]
                j+=1
            else:
                t+=s[i]
        return t



                


        
