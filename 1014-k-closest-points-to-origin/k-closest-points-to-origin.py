class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q=[]
        for x,y in points:
            dis=((x*x)+(y*y))**(0.5)
            heapq.heappush(q,[-(abs(dis)),[x,y]])
            if len(q)>k:
                heapq.heappop(q)
        ans=[]
        for _ in range(len(q)):
            ans.append(heapq.heappop(q)[1])
        return ans

        
        