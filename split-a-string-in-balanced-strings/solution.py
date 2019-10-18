# leetcode
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        l = 0
        r = 0

        for c in s:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            if l == r:
                count += 1
                l, r = 0, 0
        return count
