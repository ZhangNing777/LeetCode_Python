'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        recnct,slow,fast = head,head,head
        newhead = None
        
        while fast and fast.next:
            fast = fast.next.next 
            tmp = slow
            slow = slow.next
            tmp.next = newhead
            newhead = tmp
            
        recnct.next = slow
        a = newhead
        b = slow.next if fast else slow
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True