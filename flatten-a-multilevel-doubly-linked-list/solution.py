# leetcode
# https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/

# Definition for a Node.

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        def f(head):
            if head:
                yield head
                yield from f(head.child)
                yield from f(head.next)

        p = None
        rhead = None

        for node in f(head):
            if p:
                p.next = Node(node.val,p,None,None)
                p = p.next
            else:
                p = Node(node.val,None,None,None)
                rhead = p

        return rhead
