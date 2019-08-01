# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def f(node, n):
            if node is None:
                return 0,node
            else:
                k, next = f(node.next)
                if k+1 == n:
                    return k+1, next
                else:
                    node.next = next
                    return k+1, node
        return f(head, n)
