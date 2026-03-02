import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq=[]
        for i in range(len(nums)):
            heapq.heappush(hq,nums[i])
            if len(hq)>k:
                heapq.heappop(hq)
        print(hq)
        return heapq.heappop(hq)

        