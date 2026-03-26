class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(q,-matrix[i][j])
                if len(q)>k:
                    heapq.heappop(q)
        ans=heapq.heappop(q)
        return -ans
        