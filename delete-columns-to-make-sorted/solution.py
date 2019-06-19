# leetcode
# https://leetcode-cn.com/problems/delete-columns-to-make-sorted/
# 解题思路
# 检查不排序后的删除,直到全部都是排序列

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        D = 0
        for arr in zip(*A):
            if list(arr) != sorted(arr):
                D += 1
        return D

