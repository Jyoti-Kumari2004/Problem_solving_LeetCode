class Solution:
    def countTriples(self, n: int) -> int:
        s=set()
        for i in range(1,n+1):
            s.add(i*i)
        count=0
        for i in range(1,n):
            for j in range(1,n):
                if ((i*i)+(j*j)) in s :
                    count+=1
                    print(i,j)
        return count