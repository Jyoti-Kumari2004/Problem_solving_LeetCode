# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root:
        #     self.postorderTraversal(root.left)
        #     self.postorderTraversal(root.right)
        #     self.res.append(root.val)

        # return self.res

        # using 2 stacks
        if root is None:
            return []
        first_st=[root]
        second_st=[]
        while len(first_st)>0:
            node=first_st.pop()
            second_st.append(node)
            if node.left :
                first_st.append(node.left)
            if node.right:
                first_st.append(node.right)
        for i in range(len(second_st)):
            self.res.append(second_st.pop().val)
        return self.res