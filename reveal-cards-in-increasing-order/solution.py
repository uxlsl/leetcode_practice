# leetcode
# https://leetcode-cn.com/problems/reveal-cards-in-increasing-order/
# 相反操作

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        from collections import deque

        deck = sorted(deck, reverse=True)

        queue = deque()

        for i in deck:
            if queue:
                a = queue.pop()
                queue.appendleft(a)
            queue.appendleft(i)

        return list(queue)
