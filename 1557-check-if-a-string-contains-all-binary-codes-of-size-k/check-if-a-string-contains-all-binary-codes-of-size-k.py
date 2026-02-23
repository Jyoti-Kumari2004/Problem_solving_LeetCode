class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #efficient method
        se=set()
        if len(s)<k:
            return False
        i=0
        j=k-1
        while j<len(s):
            se.add(s[i:j+1])
            i+=1
            j+=1
        print(se)
        if len(se)==(2**k):
            return True
        return False









        #time limit excedded:
        # codes=[1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]
        # for b in range(codes[k-1]+1):
        #     bi=bin(b)
        #     bi=bi[2:]
        #     if len(bi)<k:
        #         bi="0"*(k-len(bi))+bi
        #     if bi not in s:
        #         return False
        # return True




        