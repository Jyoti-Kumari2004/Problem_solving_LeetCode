class Solution:
    def countOdds(self, low: int, high: int) -> int:
        r=high-low+1
        if low%2!=0 and high%2!=0:
            return r//2+1
        else:
            return r//2
        