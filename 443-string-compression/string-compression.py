class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        count=0
        while j<len(chars):
            chars[i]=chars[j]
            i+=1
            prev=chars[j]
            count=0
            while j<len(chars) and chars[j]==prev : 
                count+=1
                j+=1
            if count>1:
                st=list(str(count))
                for stt in st:
                    chars[i]=stt
                    i+=1
        return i
