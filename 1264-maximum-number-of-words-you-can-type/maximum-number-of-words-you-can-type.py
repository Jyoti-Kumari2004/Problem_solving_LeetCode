class Solution:
    def check(self,word: str,lt:str):
        for i in lt:
            if i in word:
                return True
            
        return False

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        words=text.split()
        for i in words:
            if self.check(i,brokenLetters)==False:
                count+=1
        return count

            
