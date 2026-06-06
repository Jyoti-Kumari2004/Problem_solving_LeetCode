class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # dd=[]
        # for word in words:
        #     d=defaultdict(int)
        #     for ch in word:
        #         d[ch]+=1
        #     dd.append(d)
        # print(dd)
        words=sorted(words,key=len)
        t=[1]*len(words)
        n=len(words)
        ans=1
        
        for i in range(n):
            maxi=1
            for j in range(i):
                if self.solve(words[i],words[j]):
                    maxi=max(maxi,1+t[j])
            t[i]=maxi
            ans=max(ans,maxi)
        return ans
    def solve(self,w1,w2):
        if len(w1)!=len(w2)+1:
            return False
        i=0
        j=0
        while i<len(w1):
            if j<len(w2) and w1[i]==w2[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j==len(w2)

                     

                
        