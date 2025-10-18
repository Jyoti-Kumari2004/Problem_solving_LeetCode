class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ip=s
        op=""
        ans=[]
        self.solve(ip,op,ans)
        return ans
    # def solve(self,ip,op,ans):
    #     if len(ip)==0:
    #         if op not in ans:
    #             ans.append(op)
    #         return
    #     op1=op
    #     op2=op
    #     if ip[0].isdigit():
    #         op1+=ip[0]
    #         op2+=ip[0]
    #     else:
    #         op1+=ip[0].lower()
    #         op2+=ip[0].upper()
    #     ip=ip[1:]
    #     self.solve(ip,op1,ans)
    #     self.solve(ip,op2,ans)
    # the above one is also correct but it has extra calls increasing repetetions and not very efficient
    

    def solve(self,ip,op,ans):
        if len(ip)==0:
            if op not in ans:
                ans.append(op)
            return
        op1=op
        op2=op
        if ip[0].isdigit():
            op1+=ip[0]
            ip=ip[1:]
            self.solve(ip,op1,ans)
            #when digit only one call
        else:
            op1+=ip[0].lower()
            op2+=ip[0].upper()
            ip=ip[1:]
            #when alpha ,it will call for 2 ..one with lower and one with upper case
            self.solve(ip,op1,ans)
            self.solve(ip,op2,ans)
        
        
        