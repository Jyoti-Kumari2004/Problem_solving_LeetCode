class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        ans=[]
        op=0
        cl=0
        for ch in s:
            if ch=='(':
                op+=1
                ans.append(ch)
                
            elif ch==')':
                if op==0:
                    continue
                op-=1
                ans.append(ch)
            else:
                ans.append(ch)
        print(ans)
        res=[]
        for ch in reversed(ans):
            if ch=='(' and op>0:
                op-=1
                continue
            res.append(ch)
        return res[::-1]



                

        