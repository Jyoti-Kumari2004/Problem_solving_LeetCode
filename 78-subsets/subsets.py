class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #this method is based on bit manipulation,take less time and less space
        # res=[]
        # n=len(nums)
        # ps=(1<<n)# power set size
        # for i in range(ps):
        #     lv=[]
        #     for j in range(n):
        #         if  ((i&(1<<j)))!=0:
        #             lv.append(nums[j])
        #     res.append(lv)
        # return res
        
        # this method is done by recurrsive tree method:
        op=[]
        ans=[]
        self.solve(nums,op,ans)
        return ans
    def solve(self,ip,op,ans):
        if len(ip)==0:
            ans.append(op)
            return
        op1=op[:] #esa isiliye kiya kyonki copy nhi ban rhi ...list is mutable to vo sab ek pe hi point karne lag gye
        op2=op[:]
        op2.append(ip[0])
        ipr=ip[1:]#same case with ip...as ip hi change ho ja rha tha (in place) we dont want it like that
        self.solve(ipr,op1,ans)
        self.solve(ipr,op2,ans)
        return
