class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lis=[[] for i in range(numRows)]
        if numRows==1:
            return s
        j=0
        direction="d"
        for i in range(len(s)):
            lis[j].append(s[i])
            if j==numRows-1:
                direction="u"
            elif j==0:
                direction="d"
            if direction=="u":
                j-=1
            else:
                j+=1
        f=""
        for l in lis:
            f+="".join(l)
        return f



        
        