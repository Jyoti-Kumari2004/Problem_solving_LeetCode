# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return ""
        s=""
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node==None:
                s+="#,"
            else:
                s+=str(node.val)+","
                q.append(node.left)
                q.append(node.right)
        print(s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=list(map(str,data.split(",")))
        if data[0]=="#" or data[0]=="":
            return None
        j=0
        q=deque()
        root=TreeNode(int(data[0]))
        q.append(root)
        
        while q:
            node=q.popleft()
            j+=1
            if data[j]=="#":
                node.left=None
            else:
                node.left=TreeNode(int(data[j])) 
                q.append(node.left)
            j+=1
            if data[j]=="#":
                node.right=None
            else:
                node.right=TreeNode(int(data[j]))
                q.append(node.right)
        return root
            

            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))