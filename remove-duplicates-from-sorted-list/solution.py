# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        first = head
        n = head.next
        head.next = None

        while n != None:
            if first.val != n.val:
                first.next = n
                first = n
                n = first.next
                first.next = None
            else:
                n = n.next

        return head
