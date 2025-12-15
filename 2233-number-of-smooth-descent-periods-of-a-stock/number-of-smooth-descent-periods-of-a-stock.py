class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count=1
        res=0
        extra_num=len(prices)
        for i in range(1,len(prices)):
            if prices[i-1]-prices[i]==1:
                count+=1
            else:
                res+=(count*(count+1))//2
                count=1
        res+=(count*(count+1))//2
        return res
                  