import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        q=[]
        for i in range(len(nums)):
            heapq.heappush(q,nums[i])
        ans=[]
        for i in range(len(q)):
            ans.append(heapq.heappop(q))
        return ans
        