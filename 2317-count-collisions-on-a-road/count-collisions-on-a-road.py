class Solution:
    def countCollisions(self, directions: str) -> int:
        str1=(directions.lstrip("L")).rstrip("R")
        count=0
        for i in str1:
            if i!="S":
                count+=1
        return count