
# leetcode 441
# https://leetcode-cn.com/problems/arranging-coins/
# 等差数列求根，也可以使用二分法查找
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = int(n**0.5)
        n = n - (1+k)*k/2
        while n - k > 0 :
            k += 1
            n -= k

        return k
