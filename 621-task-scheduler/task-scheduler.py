class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=defaultdict(int)
        for ch in tasks:
            d[ch]+=1
        q=[]
        que=deque()
        for key,value in d.items():
            heapq.heappush(q,[-value,0])
        j=0
        while q or que:
            if q:
                val,at=heapq.heappop(q)
                val+=1
                if val!=0:
                    que.append([val,j+n])
            if que and que[0][1]==j :
                v,a=que.popleft()
                heapq.heappush(q,[v,a])
            j+=1
        return j
                

        
        