# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        X = list()
        p = head

        while p is not None:
            X.append(p.val)
            p = p.next

        return self._numComponents(X, set(G))

    def _numComponents(self, X,G):

        ret = 0
        inlist = False
        for i in X:
            if i in G:
                if not inlist:
                    inlist = True
            else:
                if inlist:
                    ret += 1
                    inlist = False

        if inlist:
            ret += 1

        return ret
