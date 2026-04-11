class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch=="+":
                a=st.pop()
                b=st.pop()
                st.append(int(b)+int(a))
            elif ch=="-":
                a=st.pop()
                b=st.pop()
                st.append(int(b)-int(a))
            elif ch=="*":
                a=st.pop()
                b=st.pop()
                st.append(int(b)*int(a))
            elif ch=="/":
                a=st.pop()
                b=st.pop()
                a=int(a)
                b=int(b)
                # if a<0 and b<0:
                #     st.append(b//a)
                # elif a<0 or b<0:
                #     st.append(b//a if abs(b)>abs(a) else 0)
                # else:
                #     st.append(b//a )
                st.append(int(b/a))
            else:
                st.append(int(ch))
        return st[0]
                


        