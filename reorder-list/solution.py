# leetcode
# https://leetcode-cn.com/problems/reorder-list/
# 解法
# 链表的中点,翻转链表，二指针

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        lst = []
        p = head

        while p is not None:
            lst.append(p)
            p = p.next

        i = 1
        j = len(lst) -1
        p = head
        while i < j:
            p.next = lst[j]
            p.next.next = lst[i]
            p = p.next.next
            i += 1
            j -= 1

        if i == j:
            p.next = lst[i]
            p = p.next
        p.next = None

