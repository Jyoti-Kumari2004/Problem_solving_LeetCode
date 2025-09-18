class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        #using Moore's voting algorithm
        
        #checking for the candidate
        ele=arr[0]
        count=1
        for i in range(1,len(arr)):
            if arr[i]==ele:
                count+=1
            else:
                count-=1

            if count==0:
                ele=arr[i+1]
        
        #check if it is actually a dominatior or not
        for i in range(len(arr)):
            if arr[i]==ele:
                count+=1
        if count>len(arr)//2:
            return ele
        else:
            return -1
                

        















        #have done this using hashing O(n) time complexity and O(n) space complexity
        # n=len(nums)
        # hash=defaultdict()
        # for num in nums:
        #     if num in hash:
        #         hash[num]+=1
        #     else:
        #         hash[num]=1
        # for i in nums:
        #     if hash[i]>(n//2):
        #         return i
        