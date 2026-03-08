class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=[]
        nums=set(nums)
        self.solve(len(nums),nums,0,[],res)
        return res[0]

    def solve(self,nn,nums,ind,path,res):
        if ind==nn:
            new_path="".join(path)
            if new_path not in nums:
                res.append(new_path)
                return True
        if ind>nn:
            return False
        for i in range(ind,nn):
            path.append("1")
            if self.solve(nn,nums,ind+1,path,res):
                return True
            path.pop()
            path.append("0")
            if self.solve(nn,nums,ind+1,path,res):
                return True
            path.pop()


        