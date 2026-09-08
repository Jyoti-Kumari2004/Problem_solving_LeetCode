class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<4:
            return 0
        return abs(1000-n)+1
        