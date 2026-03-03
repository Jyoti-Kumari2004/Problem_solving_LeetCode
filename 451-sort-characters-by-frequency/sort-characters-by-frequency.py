class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for num in s:
            d[num]+=1
        q=[]
        for key,val in d.items():
            heapq.heappush(q,[-val,ord(key)])
        ans=[]
        for _ in range(len(q)):
            x,y=heapq.heappop(q)
            ans+=[chr(y) for i in range(-x)]
        return "".join(ans)
        