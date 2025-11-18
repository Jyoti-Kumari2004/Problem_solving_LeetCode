class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        if n==1:
            return True
        if n%2==0 and n>=2:
            if n>=4 and bits[-4]==0 and bits[-3]==1 and bits[-2]==1:
                return True
            if bits[-2]==0:
                return True
        else:
            if n>=5 and bits[-5]==0 and bits[-4]==bits[-3]==bits[-2]==1:
                return False
            if bits[-2]==0:
                return True
            elif bits[-3]==1 and bits[-2]==1:
                return True
            
        return False