'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
 
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
'''

from Tree import *


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def change(i):
            if not i:
                return
            change(i.left)
            if self.j:
                self.j.right,i.left = i,self.j
            else:
                self.head = i
            self.j = i
            change(i.right)

        if not root:
            return
        self.j = None
        change(root)
        self.head.left,self.j.right = self.j,self.head
        return self.head

a = Solution()
b = creatTree([4,3,6,1,2,5,7])
a.treeToDoublyList(b)