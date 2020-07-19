'''
请实现两个函数，分别用来序列化和反序列化二叉树。
'''

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
        if not root:
            return
        a,b = [],[]
        a.append(root)
        while a:
            index = a.pop(0)
            if index:
                b.append(str(index.val))
                a.append(index.left)
                a.append(index.right)
            else:
                b.append('null')

        while b[-1] == 'null':
            b.pop()

        return b
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        a = []
        i = 1
        head = TreeNode(data[0])
        a.append(head)
        while i < len(data):
            index = a.pop(0)
            if data[i] != 'null':
                index.left = TreeNode(int(data[i]))
                a.append(index.left)
            i += 1
            if i == len(data):
                break
            if data[i] != 'null':
                index.right = TreeNode(int(data[i]))
                a.append(index.right)
            i += 1
            

        return head

        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))