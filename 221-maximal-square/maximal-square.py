class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #approach 2: using dp, in approch 1 we have used dp..but here we are not solving like rectangle 
        t=[[0]*len(matrix[0]) for i in range(len(matrix))]
        ans=0
        for i in range(len(matrix)):
            if matrix[i][0]=="1":
                t[i][0]=1
                ans=max(ans,t[i][0])
        for j in range(len(matrix[0])):
            if matrix[0][j]=="1":
                t[0][j]=1
                ans=max(ans,t[0][j])
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=="1":
                    t[i][j]=1+min(t[i-1][j-1],t[i-1][j],t[i][j-1])
                    ans=max(t[i][j],ans)
                else:
                    t[i][j]=0
        print(t)
        return ans*ans
        

    #approach 1:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     li=[0]*len(matrix[0])
    #     ans=0
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j]=="1":
    #                 li[j]+=1
    #             else:
    #                 li[j]=0
    #         print(li)
    #         ans=max(self.LargestRectangleinHistogram(li),ans)
    #     return ans
    # def LargestRectangleinHistogram(self,li):
    #     x=self.nextSmaller(li)
    #     y=self.prevSmaller(li)
    #     max_area=0
    #     for i in range(len(li)):
    #         height=li[i]
    #         width=x[i]-y[i]-1
    #         if width>=height:
    #             max_area=max(max_area,height*height)
    #     return max_area



    # def prevSmaller(self,li):
    #     st=[]
    #     ans=[]
    #     for i in range(len(li)):
    #         while st and li[i]<=li[st[-1]]:
    #             st.pop()
    #         if not st:
    #             ans.append(-1)
    #         else:
    #             ans.append(st[-1])
    #         st.append(i)
    #     return ans
    
    # def nextSmaller(self,li):
    #     st=[]
    #     ans=[]
    #     for i in range(len(li)-1,-1,-1):
    #         while st and li[i]<=li[st[-1]]:
    #             st.pop()
    #         if not st:
    #             ans.append(len(li))
    #         else:
    #             ans.append(st[-1])
    #         st.append(i)
    #     return ans[::-1]