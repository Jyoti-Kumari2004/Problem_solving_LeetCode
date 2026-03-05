class Solution:
    def minOperations(self, s: str) -> int:
        count1=0
        for i in range(len(s)):
            if i%2==0 and s[i]!="0":
                count1+=1
            elif i%2==1 and s[i]!="1":
                count1+=1
        # count2=0
        # for i in range(len(s)):
        #     if i%2==0 and s[i]!="1":
        #         count2+=1
        #     elif i%2==1 and s[i]!="0":
        #         count2+=1
        return min(count1,len(s)-count1)
        
