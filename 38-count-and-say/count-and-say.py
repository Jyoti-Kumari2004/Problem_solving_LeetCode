class Solution:
    def countAndSay(self, n: int) -> str:
        curr="1"
        if n==1:
            return curr
        #ek safar song
        n=n-1
        while n>0:
            d=defaultdict(int)
            newcurr=""
            count=1
            prev=""
            j=0
            i=0
            c=0
            while j<len(curr):
                c=0
                no=curr[i]
                while j<len(curr) and curr[j]==no:
                    j+=1
                    c+=1
                #some operations
                i=j
                newcurr+=str(c)+no
            curr=newcurr
            n-=1
        return curr
