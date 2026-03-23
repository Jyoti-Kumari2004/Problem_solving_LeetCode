class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        k=1
        curr_reach=intervals[0][1]
        ans=0
        while k<len(intervals):
            # if intervals[k]==intervals[k-1]:
            #     ans+=1
            if curr_reach>intervals[k][0]:
                ans+=1
            else:
                curr_reach = intervals[k][1]
            k+=1
        return ans

