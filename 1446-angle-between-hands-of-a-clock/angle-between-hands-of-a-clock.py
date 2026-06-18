class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(360-abs(30*hour-((11*minutes)/2)),abs(30*hour-((11*minutes)/2)))