class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss=list(s.split(" "))
        j=len(ss)-1
        while j>=0 and ss[j]=="":
            print("here")
            j-=1
        return len(ss[j])
