# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getlistlen(self, head):
        total = 0
        p = head
        while p is not None:
            total += 1
            p = p.next
        return total

    def getlisttail(self, head):
        p = head
        while p.next is not None:
            p = p.next
        return p

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        length = self.getlistlen(head)
        k = k % length
        if k == 0:
            return head
        k = length - k
        p = head

        for _ in range(k-1):
            p = p.next

        new_head = p.next
        p.next = None
        tail = self.getlisttail(new_head)
        tail.next = head
        return new_head
