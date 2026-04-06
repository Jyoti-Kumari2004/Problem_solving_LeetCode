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
        self.solve(root,ans,"")
        return ans[0]

    def solve(self,root,ans,curr_sum):
        
        if root.right!=None and root.left==None:
            curr_sum+=str(root.val)
            return self.solve(root.right,ans,curr_sum)
        elif root.right==None and root.left!=None:
            curr_sum+=str(root.val)
            return self.solve(root.left,ans,curr_sum)
        elif root.left==None and root.right==None:
            curr_sum+=str(root.val)
            print(curr_sum)
            ans[0]+=int(curr_sum)
            return 
        else:
            curr_sum+=str(root.val)
            ls=self.solve(root.left,ans,curr_sum)
            rs=self.solve(root.right,ans,curr_sum)
        
        
        