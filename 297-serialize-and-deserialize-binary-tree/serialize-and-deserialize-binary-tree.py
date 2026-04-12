# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        pass


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q=deque()
        q.append(root)
        fin=[]
        while q:
            node=q.popleft()
            if node==None:
                fin.append("#,")
            else:
                fin.append(str(node.val)+",")
                q.append(node.left)
                q.append(node.right)
        s="".join(fin)
        print(s)
        return s

            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals=list(map(str,data.split(",")))
        if vals[0]=="#" or vals[0]==" ":
            return None
        root=TreeNode(int(vals[0]))
        q=deque()
        q.append(root)
        j=0
        while q:
            node=q.popleft()
            j+=1
            if vals[j]=="#":
                node.left=None
            else:
                node.left=TreeNode(int(vals[j]))
                q.append(node.left)
            j+=1
            if vals[j]=="#":
                node.right=None
            else:
                node.right=TreeNode(int(vals[j]))
                q.append(node.right)
        return root

                

        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))