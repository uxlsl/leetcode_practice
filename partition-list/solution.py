# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        a = ap = ListNode(-1)
        b = bp = ListNode(-1)
        p = head
        while p:
            if p.val < x:
                ap.next = p
                ap = p
            else:
                bp.next = p
                bp = p
            p = p.next
        bp.next = None
        ap.next = b.next
        return a.next
