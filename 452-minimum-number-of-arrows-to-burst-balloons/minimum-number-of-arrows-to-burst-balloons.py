class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        print(points)
        i=0
        j=0
        count=0
        curr_min_end=points[0][1]
        while j<len(points):
            while j<len(points) and  curr_min_end>=points[j][0]:
                curr_min_end=min(curr_min_end,points[j][1])
                j+=1
            count+=1
            i=j
            curr_min_end=points[i][1] if i<len(points) else -1
        return count
