# https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        val = 0
        result = []
        for i in A:
            val = val << 1 | i
            result.append(val % 5 == 0)

        return result
