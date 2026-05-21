class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d=defaultdict(int)
        dd=defaultdict(int)
        for i in word1:
            d[i]+=1
        for j in word2:
            dd[j]+=1
        print(d,dd)
        if len(word1)!=len(word2):
            return False
        if sorted(d)==sorted(dd) and sorted(d.values())==sorted(dd.values()):
            return True
        return False
        