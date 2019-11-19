# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.val,self.next)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        h = p
        tt = None
        head = None
        while p is not None:
            for _ in range(k - 1):
                if p.next is None:
                    if tt is not None:
                        tt.next = h
                    if head is None:
                        head = h
                    return head
                p = p.next
            if head is None:
                head = p
            t = p
            if tt is not None:
                tt.next = t
            p = p.next
            t.next = None
            self.reverseList(h)
            # h -> t
            tt = h
            h = p

        return head
