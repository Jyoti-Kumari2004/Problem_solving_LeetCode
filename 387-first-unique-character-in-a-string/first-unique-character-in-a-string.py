class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=defaultdict(int)
        for ch in s:
            d[ch]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1