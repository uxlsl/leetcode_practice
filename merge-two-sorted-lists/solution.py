# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2
        p1 = l1
        p2 = l2
        if p1.val < p2.val:
            h = p1
        else:
            # 提前吃一个
            h = p2
            p2 = p2.next
            h.next = p1
            p1 = h
        while p1.next != None and p2 != None:
            if p1.next.val > p2.val:
                pp1 = p1.next
                pp2 = p2.next
                p1.next = p2
                p2.next = pp1
                p1 = p2
                p2 = pp2
            else:
                p1 = p1.next

        if p2 != None:
            p1.next = p2

        return h
