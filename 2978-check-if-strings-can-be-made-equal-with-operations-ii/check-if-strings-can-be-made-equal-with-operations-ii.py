class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1o=[]
        s1e=[]
        s2o=[]
        s2e=[]
        for i in range(len(s1)):
            if i%2==0:
                s1e.append(s1[i])
            else:
                s1o.append(s1[i])
        for j in range(len(s2)):
            if j%2==0:
                s2e.append(s2[j])
            else:
                s2o.append(s2[j])
        # s1e.sort()
        # s1o.sort()
        # s2e.sort()
        # s2o.sort()
        # print(s1e,s2e,s1o,s2o)
        return sorted(s1e)==sorted(s2e) and sorted(s1o)==sorted(s2o)