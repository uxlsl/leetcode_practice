# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mem = set()
        p = head
        while p is not None:
            if p in mem:
                return p
            mem.add(p)
            p = p.next
        return None
