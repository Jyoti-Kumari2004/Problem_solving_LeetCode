class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        ans=0
        if not sentences:
            return 0
        for j in sentences:
            c=0
            for i in j:
                if i==" ":
                    c+=1
            ans=max(ans,c+1)

        return ans
        
        