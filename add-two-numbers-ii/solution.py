# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getnum(l):
            num = 0
            p = l
            while p is not None:
                num = num*10 + p.val
                p = p.next
            return num

        num1 = getnum(l1)
        num2 = getnum(l2)
        num3 = num1 + num2
        p = head = None

        for c in str(num3):
            if head is None:
                head = ListNode(int(c))
                p = head
            else:
                p.next = ListNode(int(c))
                p = p.next
        return head
