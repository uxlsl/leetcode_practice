# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        n = 0 # 总长
        p = head
        while p != None:
            n += 1
            p = p.next

        l = []
        r = head
        for _ in range((n+1)//2):
            l.append(r)
            r = r.next

        if len(l) >n//2:
            l.pop()

        while r != None:
            n = l.pop()
            if n.val != r.val:
                return False
            r = r.next

        return True
