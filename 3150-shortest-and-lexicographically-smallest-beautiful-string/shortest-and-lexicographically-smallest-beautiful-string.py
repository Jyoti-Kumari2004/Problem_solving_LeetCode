class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res=[]
        one=0
        i=0
        j=0
        curr_min=float('inf')
        while j<len(s):
            if s[j]=="1":
                one+=1
            
            while one>k:
                if s[i]=="1":
                    one-=1
                i+=1
            if one==k:
                temp = i
                while s[temp] == "0":
                    temp += 1
                if j-temp+1<=curr_min:
                    curr_min=j-temp+1
                    res.append(s[temp:j+1])
            j+=1
        print(res)
        if not res:
            return ""
        else:
            ans=float('inf')
            ress=res[0]
            for num in res:
                if int(num,2)<ans:
                    ress=num
                    ans=int(num,2)
            return ress
