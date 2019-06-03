# leetcode
# https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for i in A:
            if i not in seen:
                seen.add(i)
            else:
                return i

