# leetcode
# https://leetcode-cn.com/problems/next-greater-node-in-linked-list/
# Definition for singly-linked list.
import time

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        T = []

        p = head
        while p is not None:
            T.append(p.val)
            p = p.next
        m = {}
        stack = []

        for index, num in enumerate(T):
            if stack:
                a = stack[-1]
                if T[a] < num:
                    while stack:
                        x = stack.pop()
                        if T[x] < num:
                            m[x] = index
                        else:
                            stack.append(x)
                            break
                else:
                    stack.append(index)
            stack.append(index)

        ret = []
        for i in range(len(T)):
            if i in m:
                ret.append(T[m[i]])
            else:
                ret.append(0)
        return ret
