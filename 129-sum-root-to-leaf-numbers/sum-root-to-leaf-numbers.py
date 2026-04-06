# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        ans=[0]
        self.solve(root,ans,0)
        return ans[0]

    def solve(self,root,ans,curr_sum):
        if root==None:
            return 0
        if root!=None:
            curr_sum = curr_sum * 10 + root.val
        if root.left==None and root.right==None:
            ans[0]+=curr_sum
            return curr_sum
        else:
            ls=self.solve(root.left,ans,curr_sum)
            rs=self.solve(root.right,ans,curr_sum)
            return ls+rs
            
        
        
        