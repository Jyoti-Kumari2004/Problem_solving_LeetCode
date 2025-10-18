class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o=n
        c=n
        ans=[]
        op=""
        self.solve(o,c,op,ans)
        return ans
    def solve(self,o,c,op,ans):
        if o==0 and c==0:
            ans.append(op)
            return
        if o!=0:
            op1=op
            op1+="("
            self.solve(o-1,c,op1,ans)
        if o<c:
            op2=op
            op2+=")"
            self.solve(o,c-1,op2,ans)
        return
            


