class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # temp=[]
        # self.helper(res,temp,nums)
        # return res
        result=[]
        self.Permute(nums,[],result)
        return result

    def helper(self,res,temp,nums):
        if len(temp)==len(nums):
            res.append(temp.copy())
            return 
        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.helper(res,temp,nums)
            temp.pop()
    def Permute(self,ip,op,result):
        if len(ip)==0:
            result.append(op.copy())
            return 
        s=set()
        for i in range(len(ip)):
            if ip[i] not in s:
                new_ip=ip[:i]+ip[i+1:]
                op.append(ip[i])
                self.Permute(new_ip,op,result)
                op.pop()
        

        