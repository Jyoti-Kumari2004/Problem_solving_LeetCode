class Solution:
    def __init__(self):
        self.alpha=['a','b','c']
    def getHappyString(self, n: int, k: int) -> str:
        # res=[]
        # self.solve([],res,n,"",k)
        # print(res)
        # if k>len(res):
        #     return ""
        # else:
        #     return res[k-1]

        #efficient method
        ans=""
        prev=""
        total_ways=3*(1<<(n-1))
        if k>(total_ways):
            return ""
        for i in range(n):
            for ch in ['a','b','c']:
                if prev==ch:
                    continue
                rem=n-i-1
                cnt = 1 << rem
                if k>cnt:
                    k=k-cnt
                else:
                    ans+=ch
                    prev=ch
                    break
        return ans


    # def solve(self,path,res,n,prev,k):
    #     if len(path)==n:
    #         res.append("".join(path.copy()))
    #         return 
    #     if len(res)>k:
    #         return 
    #     if len(path)>n:
    #         return 
    #     for ch in self.alpha:
    #         if ch!=prev:
    #             path.append(ch)
    #             self.solve(path,res,n,ch,k)
    #             path.pop()

        