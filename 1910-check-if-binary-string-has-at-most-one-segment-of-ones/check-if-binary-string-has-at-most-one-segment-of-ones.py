class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag=False
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                flag=True
            if s[i]=="0" and flag==True:
                return False
        return True
                
