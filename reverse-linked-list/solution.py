class Solution(object):
    def _reverseList(self, p):
        if p.next is not None:
            self._reverseList(p.next).next = p
            p.next = None
        return p

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        tail = head
        while tail.next != None:
            tail = tail.next
        self._reverseList(head)
        return tail
