class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=defaultdict(int)
        h=defaultdict(int)
        for ch in ransomNote:
            d[ch]+=1
        for chh in magazine:
            h[chh]+=1
        for key,value in d.items():
            if h[key]<value:
                return False
        return True
        