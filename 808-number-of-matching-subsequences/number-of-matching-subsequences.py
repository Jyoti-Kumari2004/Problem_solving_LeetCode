class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d=defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        count=0
        for word in words:
            if len(word)<=len(s):
                if self.solve(word,d):
                    count+=1
        return count
    def solve(self,word,d):
        prev=-1
        ans=-1
        for i in range(len(word)):
            ans=-1
            s=0
            e=len(d[word[i]])-1
            while s<=e:
                mid=s+(e-s)//2
                if d[word[i]][mid]>prev:
                    ans=d[word[i]][mid]
                    e=mid-1
                else:
                    s=mid+1
            if ans==-1:
                return False
            prev=ans
        return True

        