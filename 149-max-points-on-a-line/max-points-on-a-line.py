class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans=1
        for i in range(len(points)):
            d=defaultdict(int)
            duplicates=0
            for j in range(len(points)):
                if i!=j:
                    dx=points[i][0]-points[j][0]
                    dy=points[i][1]-points[j][1]
                    if dx==0 and dy==0: duplicates+=1
                    if dx<0:
                        dx=-dx
                        dy=-dy
                    g=self.gcd(dx,dy)
                    d[(dx//g,dy//g)]+=1 
                    ans=max(ans,max(d.values(),default=0)+duplicates+1)
        return ans
    def gcd(self,a,b):
        while b:
            a, b = b, a % b
        return a