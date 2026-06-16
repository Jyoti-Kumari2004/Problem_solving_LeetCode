class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for ch in s:
            if ch=="*":
                if res:
                    res.pop()
                else:
                    continue
            elif ch=="#":
                if res:
                    res.extend(res) 
                else:
                    continue
            elif ch=="%":
                res=res[::-1]
            else:
                res.append(ch)
        return "".join(res)

        