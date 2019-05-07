# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head.next
        if p2 is None:
            return head
        while p2 and p2.next:
            tmp = p1.next
            p1.next = p2.next
            p2.next = p1.next.next
            p1.next.next = tmp
            p1 = p1.next
            p2 = p2.next
        return head
