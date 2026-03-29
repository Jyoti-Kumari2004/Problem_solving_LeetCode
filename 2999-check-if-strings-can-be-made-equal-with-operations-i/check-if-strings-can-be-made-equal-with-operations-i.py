class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s=list(s1)
        s[0],s[2]=s[2],s[0]
        if "".join(s)==s2:
            return True
        s[0],s[2]=s[2],s[0]
        s[1],s[3]=s[3],s[1]
        if "".join(s)==s2:
            return True
        s[0],s[2]=s[2],s[0]
        if "".join(s)==s2:
            return True
        return False
        
        
        