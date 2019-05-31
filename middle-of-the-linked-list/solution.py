# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        p = head
        while p:
            lst.append(p)
            p = p.next

        return lst[len(lst)//2]
