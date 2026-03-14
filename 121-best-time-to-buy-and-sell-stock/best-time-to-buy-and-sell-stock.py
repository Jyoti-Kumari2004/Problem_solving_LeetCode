class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        lmin=prices[0]
        for i in range(1,len(prices)):
            lmin=min(lmin,prices[i-1])
            ans=max(ans,prices[i]-lmin)
        return ans