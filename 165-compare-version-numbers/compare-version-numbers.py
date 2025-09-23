class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        mini=min(len(version1),len(version2))
        ver1=version1.split(".")
        ver2=version2.split(".")
        res1 =list(map(int, ver1))
        res2 = list(map(int, ver2))
        print(res1,res2)
        i=0
        j=0
        while i<len(res1) or j<len(res2):
            n1=res1[i] if i<len(res1) else 0
            n2=res2[j] if j<len(res2) else 0
            if n1>n2:
                return 1
            if n1<n2:
                return -1
            
            i+=1
            j+=1
        else:
            return 0