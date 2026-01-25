class Solution:
    def __init__(self):
        self.h=defaultdict(bool)
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.solve(s1,s2)

    def solve(self,a,b):
        if a==b:
            return True
        if len(a)<=1:
            return False
        st=a+"_"+b
        if st in self.h:
            return self.h[st]
        flag=False
        for i in range(1,len(a)):
            cond1=self.solve(a[0:i],b[len(a)-i:]) and self.solve(a[i:],b[:len(a)-i])
            cond2=self.solve(a[0:i],b[0:i]) and self.solve(a[i:],b[i:])
            if cond1 or cond2:
                flag=True
                break
            
        self.h.update({st:flag})
        return flag

        