class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count=0
        for i in s:
            if i in "aeiou":
                count+=1
        if count==0:
            return False
        else:
            return True
        