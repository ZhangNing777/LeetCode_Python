'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 
提示：
节点总数 <= 10000
'''

from typing import List
from Tree import *

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        m = []
        def remainSum(a:TreeNode, b:int, c:List[int]):
            if not a:
                return 
            c.append(a.val)
            b -= a.val
            if b == 0 and not a.left and not a.right:
                m.append(c)
            remainSum(a.left,b,c)
            remainSum(a.right,b,c)
            c.pop()

        remainSum(root,sum,[])
        return m

a = Solution()
b = creatTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(a.pathSum(b,22))
