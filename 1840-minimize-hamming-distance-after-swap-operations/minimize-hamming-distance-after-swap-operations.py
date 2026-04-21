class disjointSet:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find_parent(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find_parent(self.parent[node])
        return self.parent[node]
    def union_by_rank(self,u,v):
        
        ulp_u=self.find_parent(u)
        ulp_v=self.find_parent(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
    
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        DSU = disjointSet(len(source))
        for u,v in allowedSwaps:
            DSU.union_by_rank(u,v)
        d=defaultdict(list)
        for i in range(len(source)):
            p=DSU.find_parent(i)
            d[p].append(i)
        print(d)
        count=0
        for parent,indices in d.items():
            dd=defaultdict(int)
            for ind in indices:
                dd[source[ind]]+=1
            for jnd in indices:
                if dd[target[jnd]]>0:
                    dd[target[jnd]]-=1
                else:
                    count+=1
        return count
        
        return 0
        
        