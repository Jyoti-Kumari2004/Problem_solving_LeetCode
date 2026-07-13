class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        res=[]
        for length in range(len(str(low)),len(str(high))+1):
            for st in range(10-length):
                num=int(s[st:st+length])
                if num>=low and num<=high:
                    res.append(num)
                if num>high:
                    break
        return res
