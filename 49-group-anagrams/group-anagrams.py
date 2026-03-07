class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        for word in strs:
            res.append([word,"".join(sorted(word))])
        d=defaultdict(list)
        for word,st in res:
            d[st].append(word)
        ans=[]
        for lis in d.values():
            ans.append(lis)
        return ans
        