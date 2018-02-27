class Solution(object):
    def getlinkLength(self, head):
        l = 0
        p = head
        while p!=None:
            p = p.next
            l += 1
        return l
    def getNext(self, head, n):
        p = head
        for _ in range(n):
            p = p.next
        return p

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return False

        lA = self.getlinkLength(headA)
        lB = self.getlinkLength(headB)
        pA = headA
        pB = headB

        if lA > lB:
            pA = self.getNext(headA, lA - lB)
        elif lA < lB:
            pB = self.getNext(headB, lB - lA)

        while pA != None and pB != None:
            if pA == pB:
                return True
            pA = pA.next
            pB = pB.next

        return False
