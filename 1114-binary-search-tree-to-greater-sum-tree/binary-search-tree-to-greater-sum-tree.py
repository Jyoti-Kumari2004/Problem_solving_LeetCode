# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.anss=[]
        self.w=0
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[]
        self.inorder(root,ans)
        print(ans)
        check=[0]*len(ans)
        check[0]=sum(ans)
        for i in range(1,len(ans)):
            check[i]=check[i-1]-ans[i-1]
        print(check)
        w=0
        self.inorderA(root,check,w)
        print(self.anss)
        return root
        
        
    def inorderA(self,root,check,w):
        if root!=None:
            self.inorderA(root.left,check,self.w)
            root.val=check[self.w]
            self.anss.append(root.val)
            self.w+=1
            self.inorderA(root.right,check,self.w)
    
    def inorder(self,root,ans):
        if root!=None:
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
        
    