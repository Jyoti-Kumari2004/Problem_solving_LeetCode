class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ip=s
        op=""
        ans=[]
        self.solve(ip,op,ans)
        return ans
    def solve(self,ip,op,ans):
        if len(ip)==0:
            if op not in ans:
                ans.append(op)
            return
        op1=op
        op2=op
        if ip[0].isdigit():
            op1+=ip[0]
            op2+=ip[0]
        else:
            op1+=ip[0].lower()
            op2+=ip[0].upper()
        ip=ip[1:]
        self.solve(ip,op1,ans)
        self.solve(ip,op2,ans)
        
        