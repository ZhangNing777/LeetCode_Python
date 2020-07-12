class TreeNode(object):
    """元素节点"""
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
 
class Tree(object):
    """二叉树"""
    def __init__(self, root=None):
        self.root = root
 
    def pre_order(self, root):
      """先序遍历"""
      if root == None:
          return
      print(root.val)
      self.pre_order(root.left)
      self.pre_order(root.right)
 
    def mid_order(self, root):
        """中序遍历"""
        if root == None:
            return
        self.mid_order(root.left)
        print(root.val)
        self.mid_order(root.right)
 
    def post_order(self, root):
        """后序遍历"""
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = TreeNode(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.left)
            j += 1
            if j == len(nodeList):
                return head
            node.right = (TreeNode(nodeList[j])if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.right)
            if j == len(nodeList):
                return head
    
    


# 二叉树类
# class TreeNode(object):

#     # 初始化
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val    # 数据域
#         self.left = left    # 左子树
#         self.right = right  # 右子树

#     # 前序遍历
#     def preorder(self):

#         if self.val is not None:
#             print(self.val, end=' ')
#         if self.left is not None:
#             self.left.preorder()
#         if self.right is not None:
#             self.right.preorder()

#     # 中序遍历
#     def inorder(self):

#         if self.left is not None:
#             self.left.inorder()
#         if self.val is not None:
#             print(self.val, end=' ')
#         if self.right is not None:
#             self.right.inorder()

#     # 后序遍历
#     def postorder(self):

#         if self.left is not None:
#             self.left.postorder()
#         if self.right is not None:
#             self.right.postorder()
#         if self.val is not None:
#             print(self.val, end=' ')

#     # 层序遍历
#     def levelorder(self):

#         # 返回某个节点的左孩子
#         def LChild_Of_Node(node):
#             return node.left if node.left is not None else None
#         # 返回某个节点的右孩子
#         def RChild_Of_Node(node):
#             return node.right if node.right is not None else None

#         # 层序遍历列表
#         level_order = []
#         # 是否添加根节点中的数据
#         if self.val is not None:
#             level_order.append([self])

#         # 二叉树的高度
#         height = self.height()
#         if height >= 1:
#             # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
#             for _ in range(2, height + 1):
#                 level = []  # 该层的节点
#                 for node in level_order[-1]:
#                     # 如果左孩子非空，则添加左孩子
#                     if LChild_Of_Node(node):
#                         level.append(LChild_Of_Node(node))
#                     # 如果右孩子非空，则添加右孩子
#                     if RChild_Of_Node(node):
#                         level.append(RChild_Of_Node(node))
#                 # 如果该层非空，则添加该层
#                 if level:
#                     level_order.append(level)

#             # 取出每层中的数据
#             for i in range(0, height):  # 层数
#                 for index in range(len(level_order[i])):
#                     level_order[i][index] = level_order[i][index].val

#         return level_order

#     # 二叉树的高度
#     def height(self):
#         # 空的树高度为0, 只有root节点的树高度为1
#         if self.val is None:
#             return 0
#         elif self.left is None and self.right is None:
#             return 1
#         elif self.left is None and self.right is not None:
#             return 1 + self.right.height()
#         elif self.left is not None and self.right is None:
#             return 1 + self.left.height()
#         else:
#             return 1 + max(self.left.height(), self.right.height())

#     # 二叉树的叶子节点
#     def leaves(self):

#         if self.val is None:
#             return None
#         elif self.left is None and self.right is None:
#             print(self.val, end=' ')
#         elif self.left is None and self.right is not None:
#             self.right.leaves()
#         elif self.right is None and self.left is not None:
#             self.left.leaves()
#         else:
#             self.left.leaves()
#             self.right.leaves()