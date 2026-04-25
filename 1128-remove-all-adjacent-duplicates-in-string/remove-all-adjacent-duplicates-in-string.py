class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if st and s[i]==st[-1]:
                st.pop()
            else:
                st.append(s[i])
            i+=1
        return "".join(st)

        