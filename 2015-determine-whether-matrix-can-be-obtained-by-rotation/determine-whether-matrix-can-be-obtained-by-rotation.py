class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.compare(mat,target):
            return True
        for i in range(3):
            if self.compare(target,self.rotateMatrix(mat)):
                return True
        return False
    def rotateMatrix(self,mat1):
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if j>=i:
                    mat1[i][j],mat1[j][i]=mat1[j][i],mat1[i][j]
        for i in range(len(mat1)):
            mat1[i]=mat1[i][::-1]
        return mat1

    def compare(self,mat1,mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j]!=mat2[i][j]:
                    return False
        return True
        