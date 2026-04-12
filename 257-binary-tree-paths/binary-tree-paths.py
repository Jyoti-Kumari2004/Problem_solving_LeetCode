# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        path=[]
        self.solve(root,res,path)
        print(res)
        return res
    def solve(self,root,res,path):
        if root==None:
            return 
        if root.left==None and root.right==None:
            path.append(str(root.val))
            move="->".join(path)
            res.append(move)
            path.pop()
            return 
        path.append(str(root.val))
        self.solve(root.left,res,path)
        self.solve(root.right,res,path)
        path.pop()
        