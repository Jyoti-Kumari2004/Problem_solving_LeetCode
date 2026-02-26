class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        self.solve(n,0,[],res,"1")
        s=set()
        for ch in res:
            s.add(ch)
        return s
        

    def solve(self,n,ind,path,res,prev):
        if len(path)==n:
            path="".join(path)
            res.append(path)
            return
        for i in range(ind,n):
            if prev=="0":
                path.append("1")
                self.solve(n,i+1,path,res,"1")
                path.pop()
            else:
                path.append("0")
                self.solve(n,i+1,path,res,"0")
                path.pop()
                path.append("1")
                self.solve(n,i+1,path,res,"1")
                path.pop()
