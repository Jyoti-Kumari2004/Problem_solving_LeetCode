class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.ans=0
        self.t={}
        return self.solve(low,high,zero,one,0)%1000000007
    def solve(self,l,h,z,o,s):
        if s>h:
            return 0
        if s in self.t:
            return self.t[s]
        if l<=s<=h:
            ans= 1+self.solve(l,h,z,o,s+o)+self.solve(l,h,z,o,s+z)
        else:
            ans= self.solve(l,h,z,o,s+o)+self.solve(l,h,z,o,s+z)
        self.t[s]=ans
        return ans
        
        
