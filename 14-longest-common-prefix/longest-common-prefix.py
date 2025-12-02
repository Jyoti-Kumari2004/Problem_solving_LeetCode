class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        print(strs)
        first_word=strs[0]
        last_word=strs[-1]
        ans=""
        print(first_word)
        print(last_word)
        i=0
        if len(strs)==1:
            return strs[0]
        while i<len(first_word):
            if first_word[i]!=last_word[i]:   
                break
            ans+=first_word[i]
            i+=1
        n=len(ans)
        for i in strs:
            if (i.startswith(ans))==False: 
                return self.common_prefix(ans,i)
    
        return ans
    def common_prefix(self,a, b):
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return a[:i]
                
             
                
        

        