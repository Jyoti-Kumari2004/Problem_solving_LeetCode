#User function Template for python3
from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find_par(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_par(u)
        ulp_v = self.find_par(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds=DisjointSet(n)
        extra=0
        if (n-1>len(connections)):
            return -1
        count=0
        for u,v in connections:
           
            if ds.find_par(u)==ds.find_par(v):
                extra+=1
            else:
                ds.union_by_rank(u,v)
        for i in range(n):
            if ds.find_par(i)==i:
                count+=1
        ans=count-1
        print(count,ans)
        if extra>=ans:
            return ans
        else:
            return -1
        
        