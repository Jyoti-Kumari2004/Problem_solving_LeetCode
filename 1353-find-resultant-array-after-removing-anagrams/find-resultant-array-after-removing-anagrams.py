class Solution:
    
    def ana(self,a,b):
        if len(a)!=len(b):
            return False
        if sorted(a)!=sorted(b):
            return False
        return True
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[words[0]]
        for i in range(1,len(words)):
            if not self.ana(words[i],words[i-1]):
                ans.append(words[i])
        return ans



                


    

        