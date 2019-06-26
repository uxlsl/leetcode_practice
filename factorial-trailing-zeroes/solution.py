# leetcode
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/
# 阶乘后的零
# 参考https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/tong-guo-guan-cha-chan-sheng-ling-de-tiao-jian-er-/
# 通过观察5的个数


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n >= 5:
            res += n / 5
            n //= 5

        return res
