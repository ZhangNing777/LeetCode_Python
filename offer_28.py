'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 
限制：

0 <= 节点个数 <= 1000
'''

from Tree import *

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return(self.compare(root.right,root.left))

    def compare(self,left,right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return  False
        elif left.val != right.val:
            return False
        else:
            return(self.compare(left.left,right.right) and self.compare(left.right,right.left))



