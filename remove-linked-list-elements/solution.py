# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        h = None
        cur = head
        while cur != None:
            if cur.val != val:
                if pre is None:
                    h = cur
                else:
                    pre.next = cur
                pre = cur
                cur = cur.next
                pre.next = None
            else:
                cur = cur.next
        return h
