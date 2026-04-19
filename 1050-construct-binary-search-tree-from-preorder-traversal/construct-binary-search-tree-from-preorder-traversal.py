# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i=0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.solve(preorder,float('-inf'),float('inf'))
        
    def solve(self,preorder,mini,maxi):
        if self.i==len(preorder) or preorder[self.i]<mini or preorder[self.i]>maxi:
            return None
        root=TreeNode(preorder[self.i])
        self.i+=1 
        root.left=self.solve(preorder,mini,root.val)
        root.right=self.solve(preorder,root.val,maxi)
        return root
