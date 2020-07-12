'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
 
提示：
节点总数 <= 1000
'''
from Tree import *
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return[]
        
        a,b = [],[]
        a.append(root)
        j = 0
        while a:
            c = []
            for i in range(len(a)):
                index = a.pop(0)
                c.append(index.val)
                if index.left:
                    a.append(index.left)
                if index.right:
                    a.append(index.right)
            if j%2 == 1:
                d = []
                for i in range(len(c)-1,-1,-1):
                    d.append(c[i])
                b.append(d)
            else:
                b.append(c)
            j += 1
        return b


a = creatTree([1,2,3,4,5,None,6,7])
b = Solution()
print(b.levelOrder(a))