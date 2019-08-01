# leetcode
# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# https://www.geeksforgeeks.org/reverse-a-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        lst = []
        p = head

        while p:
            lst.append(p.val)
            p = p.next

        lst[m-1:n] = list(reversed(lst[m-1:n]))

        head = ListNode(lst[0])
        p = head

        for val in lst[1:]:
            p.next = ListNode(val)
            p = p.next

        return head
