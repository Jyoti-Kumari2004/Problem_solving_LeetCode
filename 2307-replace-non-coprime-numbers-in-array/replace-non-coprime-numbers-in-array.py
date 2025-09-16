class Solution:
    def gcd(self,a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            if a % b == 0:
                return b
            return gcd(a - b, b)
        if b % a == 0:
            return a
        return gcd(a, b - a)
    def lcm(self, a,b):
        return (a)*(b//self.gcd(a,b))
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans=[nums[0]]
        
        for i in range(1,len(nums)):
            peek=ans[-1]
            num=nums[i]
            n=self.gcd(peek,num)
            if n>1:
                ans.pop()
                ans.append(self.lcm(peek,num))
                while len(ans) > 1 and self.gcd(ans[-1], ans[-2]) > 1:
                    b = ans.pop()
                    a = ans.pop()
                    ans.append(self.lcm(a, b))
                
            else:
                ans.append(nums[i])
        return ans
                





        