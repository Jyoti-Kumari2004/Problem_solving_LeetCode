class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m=list(pattern)
        mp=s.split(" ")
        if len(m)!=len(mp):
            return False
        d=defaultdict(int)
        dd=defaultdict(int)
        for i in range(len(mp)):
            if mp[i] not in d and m[i] not in dd:
                d[mp[i]]=m[i]
                dd[m[i]]=mp[i]
            else:
                if d[mp[i]]!=m[i] or dd[m[i]]!=mp[i]:
                    return False

        return True
                
        