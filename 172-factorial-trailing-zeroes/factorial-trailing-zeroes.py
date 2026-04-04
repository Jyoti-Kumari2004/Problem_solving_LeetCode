class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        curr=5
        while curr<=n:
            count+=n//curr
            curr=curr*5
        return count
            
        