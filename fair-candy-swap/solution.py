# leetcode
# https://leetcode-cn.com/problems/fair-candy-swap/

# 提示,二者相等


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        total_a = sum(A)
        total_b = sum(B)
        target = (total_a + total_b) // 2

        B = set(B)
        for i in A:
            j = target - total_a + i
            if j in B:
                return [i,j]

