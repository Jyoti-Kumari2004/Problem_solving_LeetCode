class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        count=0
        intervals.sort()
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]>=intervals[j][0]:
                    count+=1
        return count
