# leetcode
# https://leetcode-cn.com/problems/moving-stones-until-consecutive/
# 解法
# 最大值间隔的情况分类


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        a, b, c = sorted([a, b, c])
        if c - b == 1 and b - a == 1:
            x = 0
        elif c - b >= 3 and b - a >= 3:
            x = 2
        else:
            x = 1
        y = c - a - 2

        return [x, y]
