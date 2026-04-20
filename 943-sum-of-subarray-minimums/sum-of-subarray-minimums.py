class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ns=self.nextsmaller(arr)
        ps=self.prevsmaller(arr)
        count=0
        for i in range(len(arr)): 
            l=ns[i]-i
            r=i-ps[i]
            count+=l*r*arr[i]
        return count%1000000007

    def nextsmaller(self,arr):
        ans=[]
        st=[]
        n=len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if not st:
                ans.append(len(arr))
            else:
                ans.append(st[-1])
            st.append(i)
        return ans[::-1]
    def prevsmaller(self,arr):
        ans=[]
        st=[]
        n=len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])
            st.append(i)
        return ans

        