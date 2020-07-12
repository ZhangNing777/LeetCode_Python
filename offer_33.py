'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 
提示：

数组长度 <= 1000
'''

from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        if len(postorder) == 0:
            return True

        a = postorder[-1]

        for i in range(len(postorder)):
            if postorder[i] > a:
                break
        
        for j in range(i,len(postorder)):
            if postorder[j] < a:
                return False

        if i > 0:
            left = self.verifyPostorder(postorder[0:i])
        else:
            left = True

        if i < len(postorder)-1:
            right = self.verifyPostorder(postorder[i:len(postorder)-1])
        else:
            right = True

        return right&left

a = Solution()
print(a.verifyPostorder([]))