import sys
sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(100000)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        num=int(num)
        while num:
            if num%2==1:
                return str(num)
            num=num//10
        return ""
