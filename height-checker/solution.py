# leetcode
# https://leetcode-cn.com/problems/height-checker/


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        for x,y in zip(heights, sorted(heights)):
            if x != y:
                res += 1
        return res

