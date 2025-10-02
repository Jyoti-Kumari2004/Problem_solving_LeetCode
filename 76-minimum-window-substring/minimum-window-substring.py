class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i,j,count=0,0,0
        m=float('inf')
        res=""
        map=defaultdict(int)
        for ch in t:
            map[ch]+=1
        count=len(map)
        print(map)
        while j<len(s):
            if s[j] in map:
                map[s[j]]-=1
                if map[s[j]]==0:
                    count-=1   
            #slid and check upto that number
            while count==0:
                if j-i+1<m:
                    m=(j-i+1)
                    res=s[i:i+m]
                if s[i] in map:
                    map[s[i]]+=1
                    if map[s[i]]==1:
                        count+=1
                i+=1
            j+=1
        return res


        
