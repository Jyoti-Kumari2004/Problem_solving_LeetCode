# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        st=[]
        self.roots(root1,st)
        st1=[]
        self.roots(root2,st1)
        print(st,st1)
        return st==st1

    def roots(self,root,st):
        if root.left==None and root.right==None:
            st.append(root.val)
        elif root.left==None:
            self.roots(root.right,st)
        elif root.right==None:
            self.roots(root.left,st)
        else:
            self.roots(root.left,st)
            self.roots(root.right,st)


        