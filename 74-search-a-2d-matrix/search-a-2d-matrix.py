class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix[0])
        n=len(matrix)
        i=0
        j=m-1
        while i>=0 and i<n and j>=0 and j<m:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False