class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        curr=0
        if k==len(num):
            return "0"
        for i in range(len(num)):
            while st and st[-1]>num[i]and curr<k:
                st.pop()
                curr+=1
            st.append(num[i])
        print(curr,k)
        print(st)
        if curr<k and st:
            while curr<k and st:
                st.pop()
                curr+=1
        res="".join(st).lstrip("0")
        return res if res else "0"

        