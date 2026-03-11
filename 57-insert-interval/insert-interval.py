class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        i=0
        new_mini=newInterval[0]
        new_maxi=newInterval[1]
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        while i<len(intervals) and intervals[i][0] <= new_maxi:
            new_mini=min(new_mini,intervals[i][0])
            new_maxi=max(new_maxi,intervals[i][1])
            i+=1
        ans.append([new_mini,new_maxi])
        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans
        

        