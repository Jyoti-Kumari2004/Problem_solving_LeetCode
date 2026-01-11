# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s=self.summ(root)
        self.dfs(root,s)
        return self.ans%1000000007
    def dfs(self,root,s):
        if root==None:
            return 0
        ls=self.dfs(root.left,s)
        rs=self.dfs(root.right,s)
        curr_sum=ls+rs+root.val
        self.ans=max(self.ans,((s-curr_sum)*curr_sum))
        return curr_sum

    
        
    def summ(self,root):
        if root==None:
            return 0
        r=self.summ(root.right)
        l=self.summ(root.left)
        return root.val+r+l
        