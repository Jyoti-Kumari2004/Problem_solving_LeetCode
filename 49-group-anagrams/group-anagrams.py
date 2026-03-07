class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for st in strs:
            t=[0]*26
            for j in st:
                t[ord(j)-ord('a')]+=1
            d[tuple(t)].append(st)
        print(d)
        return list(d.values())



        #this is one method
        # res=[]
        # for word in strs:
        #     res.append([word,"".join(sorted(word))])
        # d=defaultdict(list)
        # for word,st in res:
        #     d[st].append(word)
        # ans=[]
        # for lis in d.values():
        #     ans.append(lis)
        # return ans
        