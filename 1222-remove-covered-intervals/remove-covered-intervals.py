class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        print(intervals)
        i=0
        j=1
        n=len(intervals)
        if n==1:
            return 1
        while j<len(intervals):
            if intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                n-=1
                j+=1
            else:
                i=j
                j+=1
        return n