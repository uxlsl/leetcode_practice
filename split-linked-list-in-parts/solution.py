# leetcode
# https://leetcode-cn.com/problems/split-linked-list-in-parts/
# 解法:
# 求长度

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        p = root
        while p is not None:
            length += 1
            p = p.next

        avg = length // k
        residue = length % k
        ret = []
        p = root
        pp = None

        for _ in range(k):
            ret.append(p)
            for _ in range(avg):
                if p is not None:
                    pp,p = p, p.next
            if residue > 0:
                if p is not None:
                    pp,p = p, p.next
                residue -= 1
            if pp:
                pp.next = None
        return ret
