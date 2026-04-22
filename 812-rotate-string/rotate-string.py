class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        news=s+s
        j=len(s)
        i=0
        while j<len(news):
            if news[i:j]==goal:
                return True
            j+=1
            i+=1
        return False

        #worst method to use
        # for i in range(len(s)):
        #     ele1=s[:i]
        #     ele11=ele1[::-1]
        #     ele2=s[i:]
        #     ele22=ele2[::-1]
        #     ele3=ele11+ele22
        #     new_s=ele3[::-1]
        #     if new_s==goal:
        #         return True
        # return False

        
    
        