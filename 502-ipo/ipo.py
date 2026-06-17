class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mini=[[cap,pro] for pro,cap in zip(profits,capital)]
        maxi=[]
        heapq.heapify(mini)
            
        for i in range(k):
            while mini and mini[0][0]<=w:
                c,p=heapq.heappop(mini)
                heapq.heappush(maxi,-p)
            w+=-heapq.heappop(maxi) if maxi else 0
        return w
        