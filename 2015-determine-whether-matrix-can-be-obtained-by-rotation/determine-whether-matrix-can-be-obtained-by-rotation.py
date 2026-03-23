class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        new_mat=mat
        for i in range(4):
            new_mat=self.rotateMatrix(new_mat)
            if self.compare(target,new_mat):
                return True
        return False
    def rotateMatrix(self,mat1):
        mat2=[[0 for i in range(len(mat1))] for i in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                mat2[i][j]=mat1[j][i]
        for i in range(len(mat2)):
            mat2[i]=mat2[i][::-1]
        return mat2

    def compare(self,mat1,mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j]!=mat2[i][j]:
                    return False
        return True
        