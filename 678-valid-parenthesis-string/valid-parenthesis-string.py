class Solution:
    def __init__(self):
        self.t=[[-1]*101 for i in range(101)]
    def checkValidString(self, s: str) -> bool:
        count=0
        return self.solve(s)
        
    #multiple approaches:
    def solve(self,s):
        st1=[]
        st2=[]
        for i,ch in enumerate(s):
            if ch=="(":
                st1.append(i)
            elif ch=="*":
                st2.append(i)
            else:
                #")"
                if st1:
                    st1.pop()
                elif st2:
                    st2.pop()
                else:
                    return False
        while st2 and st1:
            if st2[-1]>st1[-1]:
                st1.pop()
            st2.pop()
            
        if len(st1)>0:
            return False
        return True


    #3.Top-bottom approach
    # def solve(self,s):
    #     n=len(s)
    #     m=len(s)
    #     t=[[False]*(m+1) for i in range(n+1)]
    #     t[0][0]=True
    #     for i in range(1,n+1):
    #         for j in range(m+1):
    #             if s[i-1]=="(" and j-1>=0:
    #                 t[i][j]=t[i-1][j-1]
    #             elif s[i-1]==")" and j+1<m:
    #                 t[i][j]=t[i-1][j+1]
    #             else:
    #                 if j-1>=0 and j+1<m:
    #                     t[i][j]=t[i-1][j-1] or t[i-1][j+1] or t[i-1][j]
    #                 elif j-1>=0:
    #                     t[i][j]=t[i-1][j-1] or t[i-1][j]
    #                 elif j+1<m:
    #                     t[i][j]=t[i-1][j+1] or t[i-1][j]
    #                 else:
    #                     t[i][j]=t[i-1][j]

    #     return t[n][0]


    # #2.bottom-up
    # def solve(self,s,ind,count):
    #     print("hi")
    #     if ind==len(s):
    #         return count==0
    #     if count<0:
    #         return False
    #     if self.t[ind][count]!=-1:
    #         return self.t[ind][count]
    #     if s[ind]=="*":
    #         res=self.solve(s,ind+1,count) or self.solve(s,ind+1,count-1) or self.solve(s,ind+1,count+1)
    #     if s[ind]=="(":
    #         res=self.solve(s,ind+1,count+1)
    #     if s[ind]==")":
    #         res=self.solve(s,ind+1,count-1)
    #     self.t[ind][count]=res
    #     return res


    # #1.Recurrsion
    # def solve(self,s,ind,count):
    #     if ind==len(s):
    #         return count==0
    #     if count<0:
    #         return False
    #     if s[ind]=="*":
    #         return self.solve(s,ind+1,count) or self.solve(s,ind+1,count-1) or self.solve(s,ind+1,count+1)
    #     if s[ind]=="(":
    #         return self.solve(s,ind+1,count+1)
    #     if s[ind]==")":
    #         return self.solve(s,ind+1,count-1)
    #     return False




       
        




       
        