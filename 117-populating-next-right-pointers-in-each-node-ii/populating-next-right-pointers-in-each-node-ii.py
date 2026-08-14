"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return root
        q=deque()
        q.append(root)
        res=[]
        while q:
            lis=[]
            l=len(lis)
            for i in range(len(q)):
                node=q.popleft()
                lis.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(lis)):
                if i!=len(lis)-1:
                    lis[i].next=lis[i+1]

            
        return root

                
                    

        