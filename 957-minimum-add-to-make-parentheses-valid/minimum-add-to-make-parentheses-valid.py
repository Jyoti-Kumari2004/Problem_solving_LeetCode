class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        cl=0
        op=0
        for ch in s:
            if ch=="(":
                op+=1
            elif ch==")":
                if op>0:
                    op-=1
                else:
                    cl+=1
        return cl+op

        