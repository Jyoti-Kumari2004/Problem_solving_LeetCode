import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dg=0
        area=0
        for i in dimensions:
            l=i[0]
            w=i[1]
            d=math.sqrt((l*l)+(w*w))
            if d>dg:
                dg=d
                area=l*w
            elif d==dg:
                area=max(area,l*w)
        return area

            
            
            
            
    