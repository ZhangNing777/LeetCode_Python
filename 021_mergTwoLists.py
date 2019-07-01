'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = b = ListNode(0)
        
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                m = l1.val
                n = l2.val
                if m < n:
                    a.next = ListNode(m)
                    l1 = l1.next
                else:
                    a.next = ListNode(n)
                    l2 = l2.next
            elif l1 != None:
                a.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 != None:
                a.next = ListNode(l2.val)
                l2 = l2.next
            a = a.next
        return b.next
