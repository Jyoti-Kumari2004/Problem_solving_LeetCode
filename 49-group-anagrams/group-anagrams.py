class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=[]
        for i in range(len(strs)):
            d=defaultdict(int)
            for j in strs[i]:
                d[j]+=1
            sorted_dict = dict(sorted(d.items()))
            li.append(sorted_dict)
        res=[]
        visited=[False]*len(strs)
        print(li)
        for j in range(len(li)):
            ans=[]
            for k in range(len(li)):
                if li[j]==li[k] and visited[k]==False:
                    ans.append(strs[k])
                    visited[k]=True
            if ans:
                ans.sort()
                res.append(ans)
        res.sort()
        return res
            