class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q=[]
        for i in range(len(arr)):
            heapq.heappush(q,[-(abs(arr[i]-x)),-arr[i]])
            if len(q)>k:
                heapq.heappop(q)
        ans=[]
        for i in range(len(q)):
            ans.append(-(heapq.heappop(q)[1]))
        ans.sort()
        return ans
        
