# leetcode
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# 1. 过滤重复
# 2. 去掉重复
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}>{}'.format(self.val, self.next)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def f(p1, p2):
            if p2 is None:
                return p1
            if p1 is None:
                return None

            if p1.val != p2.val:
                p1.next = f(p2, p2.next)
                return p1
            else:
                p = p2
                while p is not None and p1.val == p.val:
                    p = p.next
                if p is not None:
                    return f(p, p.next)
                else:
                    return None
        if head is None:
            return None
        return f(head, head.next)
