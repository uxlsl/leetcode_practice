# Definition for singly-linked list.
import time
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.val, self.next)


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        p = head.next
        head.next = None

        while p is not None:
            next = p.next
            p.next = None
            head = self.insertOne(head, p)
            p = next

        return head

    def insertOne(self, head, node):
        if head.val >= node.val:
            node.next = head
            return node

        p = head
        while p is not None and p.next is not None:
            if node.val <= p.next.val:
                p.next,node.next = node,p.next
                return head
            p = p.next
        p.next = node
        return head
