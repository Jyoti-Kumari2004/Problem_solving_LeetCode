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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d=defaultdict(int)
        ds=DisjointSet(len(accounts))
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in d:
                    d[mail]=i
                else:
                    ds.union_by_rank(i,d[mail])
        print(d)
        #now you have this whole relation just need to put in a merged mail
        ans=[[]for i in range(len(accounts))]
        for mail in d:
            node=ds.find_par(d[mail])
            ans[node].append(mail)
        print(ans)

        res=[]
        for i in range(len(accounts)):
            if len(ans[i])==0:
                continue
            temp=[]
            temp.append(accounts[i][0])
            ans[i]=sorted(ans[i])
            for j in ans[i]:
                temp.append(j)
            res.append(temp)
        return res

        









