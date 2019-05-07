# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def GetListLength(self, p):
        result = 0
        while p:
            result += 1
            p = p.next
        return result

    def GetNode(self, p,index):
        length = self.GetListLength(p)
        for _ in range(index):
            p = p.next
        return p

    def mergeList(self,p1, p2):
        if p1.val < p2.val:
            head = p1
        else:
            head = p2
            p1,p2 = p2,p1
        while p1.next and p2:
            if p1.val <= p2.val < p1.next.val:
                p3 = p1.next
                p4 = p2.next
                p1.next = p2
                p2.next = p3
                p2 = p4
            p1 = p1.next
        if p2:
            p1.next = p2
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = self.GetListLength(head)
        if length <= 1:
            return head
        p = self.GetNode(head, length//2-1)
        m = p.next
        p.next = None
        p1 = self.sortList(head)
        p2 = self.sortList(m)
        return self.mergeList(p1, p2)
