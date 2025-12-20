# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans=[]
        self.inorder(root,ans)
        i=0
        j=len(ans)-1
        while i<j:
            if ans[i]+ans[j]==k:
                return True
            elif ans[i]+ans[j]>k:
                j-=1
            else:
                i+=1
        return False




    def inorder(self,root,ans):
        if root!=None:
            
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
        




        