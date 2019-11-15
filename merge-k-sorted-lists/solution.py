# Definition for singly-linked list.
# 最简单方法，化为列表，排序，再组装链表
# 递归组装二条链表开始


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = head = None
        x = [i for i in lists if i is not None]

        while x:
            pos = 0
            for i in range(1, len(x)):
                if x[i].val < x[pos].val:
                    pos = i

            if head is None:
                p = head = ListNode(x[pos].val)
            else:
                p.next = ListNode(x[pos].val)
                p = p.next

            x[pos] = x[pos].next
            if x[pos] is None:
                del x[pos]

        return head
