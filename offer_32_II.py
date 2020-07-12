'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return[]
        
        a,b = [],[]
        a.append(root)
        while a:
            c = []
            for i in range(len(a)):
                index = a.pop(0)
                c.append(index.val)
                if index.left:
                    a.append(index.left)
                if index.right:
                    a.append(index.right)
            b.append(c)
        return b