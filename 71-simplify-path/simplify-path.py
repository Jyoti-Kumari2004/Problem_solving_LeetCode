class Solution:
    def __init__(self):
        self.alph={'a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    def simplifyPath(self, path: str) -> str:
        vals=path.split("/")
        print(vals)
        st=[]
        for ch in vals:
            if ch==""or ch==".":
                continue
            if ch=="..":
                if st:
                    st.pop()
                else:
                    continue
            else:
                st.append(ch) 
        if not st:
            return "/"       
        ans=""
        for ch in st:
            ans+="/"+ch
        return ans
        