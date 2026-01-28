class TrieNode:
    def __init__(self):
        self.links=[None]*2
    def containskey(self,bit):
        return self.links[bit] is not None
    def put(self,bit,node):
        self.links[bit]=node
    def get(self,bit):
        return self.links[bit]
    
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

    def maximizeXor(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr.sort()
        offline_Queries=[]
        for i in range(len(queries)):
            offline_Queries.append((queries[i][0],queries[i][1],i))
        #offline queries mi ke basis pe sort kar li....
        offline_Queries.sort(key=lambda x: x[1])
        print(offline_Queries)
        idx=0
        ans=[0]*len(offline_Queries)
        trie=Solution()
        n=len(arr)
        for i in range(len(offline_Queries)):
            xi,ai,qidx=offline_Queries[i]
            while n>idx and arr[idx]<=ai:
                trie.insert(arr[idx])
                idx+=1
            if idx==0:
                ans[qidx]=-1
            else:
                ans[qidx]=trie.getMax(xi)
        return ans





        