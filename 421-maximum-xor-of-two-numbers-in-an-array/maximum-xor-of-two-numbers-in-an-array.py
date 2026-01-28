class TrieNode:
    def __init__(self):
        self.links=[None]*2
    def containskey(self,ind):
        return self.links[ind] is not None
    def put(self,ind,node):
        self.links[ind]=node
    def get(self,ind):
        return self.links[ind]
    



class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,num):
        node=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if not node.containskey(bit):
                node.put(bit,TrieNode())
            node=node.get(bit)

    def getMax(self,num):
        node=self.root
        maxNum=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if node.containskey(1-bit):
                maxNum=maxNum | (1<<i)
                node=node.get(1-bit)
            else:
                node=node.get(bit)
        return maxNum


    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Solution()
        for num in nums:
            trie.insert(num)
        maxi=float('-inf')
        for num in nums:
            maxi=max(maxi,trie.getMax(num))
        return maxi
        
        
        