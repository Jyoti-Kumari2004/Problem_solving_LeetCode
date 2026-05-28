# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxpath=0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxpath=0
        self.maxZigZag(root,0,True)
        return self.maxpath
        
    def maxZigZag(self,node,steps,direction):
        if node==None:
            return 
        self.maxpath=max(steps,self.maxpath)
        if direction==True:
            self.maxZigZag(node.right,steps+1,False)
            self.maxZigZag(node.left,1,True)
        else:
            self.maxZigZag(node.left,steps+1,True)
            self.maxZigZag(node.right,1,False)

        
        
        