class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr=[]
        num=n//2
        if n%2==0:
            for i in range(n):
                arr.append(num)
                if num==1:
                    num-=1
                num=num-1
                
        else:
            for i in range(n):
                arr.append(num)
                num=num-1

        return sorted(arr)

        