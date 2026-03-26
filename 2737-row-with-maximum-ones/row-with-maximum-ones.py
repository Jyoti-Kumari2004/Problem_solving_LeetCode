class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans=[0]*len(mat)
        for i in range(len(mat)):
            curr=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    curr+=1
            ans[i]=curr
        res=0
        maxi=ans[0]
        for i in range(len(ans)):
            if ans[i]>maxi:
                maxi=ans[i]
                res=i
        return [res,maxi]


    
        