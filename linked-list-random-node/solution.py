# leetcode
# https://leetcode-cn.com/problems/linked-list-random-node/
# 蓄水池算法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        lst = []
        p = head
        while p is not None:
            lst.append(p)
            p = p.next
        self.lst = lst


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.choice(self.lst)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
