# leetcode
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/
# 解法
# 排序,组差别正好为1的解,然后求最大的


from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        a = Counter(nums).most_common()
        if len(a) == 1:
            return 0
        a = sorted(a, key=lambda x:x[0])
        l = None
        for i in range(0, len(a)-1):
            if abs(a[i][0] - a[i+1][0])<=1:
                if l is None:
                    l = a[i][1] + a[i+1][1]
                else:
                    l = max(l, a[i][1] + a[i+1][1])
        if l:
            return l
        return 0
