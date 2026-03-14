class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        ans[-1]=0
        st=[]
        for i in range(len(ans)-1,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if not st:
                ans[i]=0
            else:
                ans[i]=st[-1]-i
            st.append(i)
        return ans
        
                




            



        