class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        l1=matrix[0]
        prev=list(map(int, l1))
        
        ans=self.getMaxArea(list(map(int, l1)))
        for i in range(1,len(matrix)):
            li=[]
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    li.append(int(matrix[i][j])+prev[j])
                else:
                    li.append(0)
                temp=self.getMaxArea(list(map(int, li)))
                ans=max(ans,temp)
            prev=li
        return ans
        


        
    def getMaxArea(self, arr):
        # code here
        ns=self.nextSmaller(arr)
        ps=self.prevSmaller(arr)
        area=0
        
        for i in range(len(arr)):
            height=arr[i]
            width=ns[i]-ps[i]-1
            area=max(area,height*width)
        return area
            
    def nextSmaller(self,arr):
        st=[]
        res=[]
        for i  in range(len(arr)-1,-1,-1):
            if not st:
                res.append(len(arr))
            elif arr[st[-1]]<arr[i]:
                res.append(st[-1])
            else:
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if not st:
                    res.append(len(arr))
                else:
                    res.append(st[-1])
            st.append(i)
        return res[::-1]
    def prevSmaller(self,arr):
        st=[]
        res=[]
        for i  in range(len(arr)):
            if not st:
                res.append(-1)
            elif arr[st[-1]]<arr[i]:
                res.append(st[-1])
            else:
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if not st:
                    res.append(-1)
                else:
                    res.append(st[-1])
            st.append(i)
        return res
        
        