"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        import copy
        m = {}
        p1 = head
        head2 = copy.copy(p1)
        p2 = head2
        while p1:
            m[p1] = p2
            p1 = p1.next
            p2.next = copy.copy(p1)
            p2 = p2.next

        p1 = head
        p2 = head2
        while p1:
            if p1.random:
                p2.random = m[p1.random]
            p1 = p1.next
            p2 = p2.next
        return head2
