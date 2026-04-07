# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # q=[]
        # self.solve(root,q,k)
        # return -q[0]

        #second approach
        res=[]
        self.solveEffi(root,res,k)
        return res[-1]

    def solveEffi(self,root,res,k):
        if root==None:
            return False
        ls=self.solveEffi(root.left,res,k)
        if ls :return True
        res.append(root.val)
        print(res)
        if len(res)==k:
            return True
        rs=self.solveEffi(root.right,res,k)
        if rs:return True
        




    #since this method is inefficient , as this take O(no.of nodes),but we can solve this in O(n) property
    # def solve(self,root,q,k):
    #     if root!=None:
    #         heapq.heappush(q,-root.val) 
    #         if len(q)>k:
    #             heapq.heappop(q)
    #         self.solve(root.right,q,k)
    #         self.solve(root.left,q,k)
    

        