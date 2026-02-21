class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        for ch in s1:
            arr1[ord(ch)-ord('a')]+=1
        i=0
        j=0
        while j<len(s2):
            arr2[ord(s2[j])-ord('a')]+=1
            if (j-i+1)>len(s1):
                arr2[ord(s2[i])-ord('a')]-=1
                i+=1
            if (j-i+1)==len(s1) and arr1==arr2:
                return True
            
            j+=1
        return False

        