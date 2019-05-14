# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        head_pre = ListNode(None)
        head_pre.next = head
        p = head_pre
        while p and p.next and p.next.next:
            a,b,c,d = p,p.next,p.next.next,p.next.next.next
            a.next = c
            c.next = b
            b.next = d
            p = p.next.next
        return head_pre.next
