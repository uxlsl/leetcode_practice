# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getlistnum(self,l):
        total = 0
        count = 0
        p = l
        while p is not None:
            total = p.val * 10**count + total
            count += 1
            p = p.next
        return total

    def convertNumberToList(self,number):
        head = p = ListNode(number%10)
        number = number // 10
        while number > 0:
            p.next = ListNode(number%10)
            number = number // 10
            p = p.next
        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.getlistnum(l1)
        b = self.getlistnum(l2)
        c = a + b
        return self.convertNumberToList(c)
