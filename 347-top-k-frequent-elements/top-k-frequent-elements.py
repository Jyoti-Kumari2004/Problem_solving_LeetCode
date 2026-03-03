class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        q=[]
        for num in nums:
            d[num]+=1
        for key,val in d.items():
            heapq.heappush(q,[val,key])
            if len(q)>k:
                heapq.heappop(q)
        ans=[]
        print(q)
        for i in range(len(q)):
            ans.append(heapq.heappop(q)[1])
        return ans

        
        