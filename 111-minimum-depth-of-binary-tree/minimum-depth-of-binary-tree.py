# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        self.ans=[]
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=deque()
        q.append(root)
        while len(q)>0:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(str(node.val))
                if node.left==node.right==None:
                    return len(self.ans)+1
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            self.ans.append(level)  

        return 0
        