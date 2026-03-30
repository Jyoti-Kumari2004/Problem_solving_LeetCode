class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odalpha=[0]*26
        evalpha=[0]*26

        for i in range(len(s1)):
            if i%2==0:
                odalpha[ord('a')-ord(s1[i])]+=1
            else:
                evalpha[ord('a')-ord(s1[i])]+=1
        for j in range(len(s2)):
            if j%2==0:
                odalpha[ord('a')-ord(s2[j])]-=1
            else:
                evalpha[ord('a')-ord(s2[j])]-=1
        for i in range(len(odalpha)):
            if odalpha[i]!=0 or evalpha[i]!=0:
                return False
        return True
        
