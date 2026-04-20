class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d=defaultdict(int)
        for num in hand:
            d[num]+=1
        while d:
            i=min(d)
            count=0
            while i in d:
                count+=1
                d[i]-=1
                if d[i]==0:
                    del d[i]
                if count==groupSize:
                    break
                i+=1
            if count<groupSize:
                return False
        return True
            
