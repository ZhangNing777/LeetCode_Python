'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
'''

from Tree import *
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        a,b = [],[]
        a.append(root)
        while a:
            index = a.pop(0)
            b.append(index.val)
            if index.left:
                a.append(index.left)
            if index.right:
                a.append(index.right)

        return b




a = creatTree([1,2,3,4,5,None,6,7])
b = Solution()
print(b.levelOrder(a))
