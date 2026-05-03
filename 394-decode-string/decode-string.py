class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if s[i]=="]":
                temp=[]
                while st and st[-1]!="[":
                    temp.append(st.pop())
                temp=temp[::-1]
                chi="".join(temp)
                st.pop()
                m=st.pop()
                st.append(m*chi)
                i+=1
            elif s[i].isalpha():
                num=""
                while i<len(s) and s[i].isalpha():
                    num+=s[i]
                    i+=1
                st.append(num)
            elif s[i].isdigit():
                num=""
                while i<len(s) and s[i].isdigit():
                    num+=s[i]
                    i+=1
                st.append(int(num))
            else:
                st.append(s[i])
                i+=1
        return "".join(st)
            
                
        