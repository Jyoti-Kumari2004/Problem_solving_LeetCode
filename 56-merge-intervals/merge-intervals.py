class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        k=0
        intervals.sort() #taking nlogn time
        curr_reach=max(intervals[0])
        i=0
        ans=[]
        while k<len(intervals):
            if min(intervals[k])<=curr_reach:
                curr_reach=max(curr_reach,intervals[k][1])
            else:
                ans.append([intervals[i][0],curr_reach])
                curr_reach=intervals[k][1]
                i=k
            k+=1
        ans.append([intervals[i][0],curr_reach])
        return ans

        