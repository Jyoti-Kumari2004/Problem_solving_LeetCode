class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        q=[]
        for key,val in d.items():
            heapq.heappush(q,[val,-key])
        ans=[]
        print(q)
        for _ in range(len(q)):
            x,y=heapq.heappop(q)
            ans+=[-y for i in range(x)]
        return ans

        