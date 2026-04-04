class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        r=rows
        c=len(encodedText)//rows
        s=encodedText
        table=[[None]*c for i in range(r)]
        k=0
        for i in range(r):
            for j in range(c):
                table[i][j]=s[k]
                k+=1
        i=0
        ans=""
        k=0
        while k<c:
            i=k
            j=0
            while j<r and i<c:
                ans+=table[j][i] 
                j+=1
                i+=1
                
            k+=1
        return ans.rstrip()



       
        