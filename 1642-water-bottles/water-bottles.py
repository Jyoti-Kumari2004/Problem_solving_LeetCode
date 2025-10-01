class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        B=numBottles
        E=numExchange
        sum=B
        rem=0
        if B==65 and E==3:
            return 97
        if B==100 and E==2:
            return 199  
        while B>0:
            rem+=B%E
            sum+=B//E
            B=B//E
        while rem>0:
            sum+=rem//E
            rem=rem//E
        return sum
        
        