class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # if sum(capacity)>=sum(apple):
        #     return len(capacity)
        capacity.sort(reverse=True)
        print(capacity)
        count=0
        i=0
        s=0
        while s<sum(apple) and i<len(capacity):
            s+=capacity[i]
            i+=1
            count+=1
        return count
        