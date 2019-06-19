# 数组的度
# leetcode 697
# https://leetcode-cn.com/problems/degree-of-an-array/submissions/

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 找最大频数,然后找出首次出现和最后出现
        from collections import defaultdict
        if len(nums) == 1:
            return 1
        m = defaultdict(int)
        first = {}
        last = {}

        for index,value in enumerate(nums):
            m[value] += 1
            if value not in first:
                first[value] = index
            last[value] = index

        if len(m) == 1:
            return len(nums)

        m = sorted(m.items(), key=lambda x:x[1], reverse=True)

        m0 = m[0] # 出现次数
        result = last[m0[0]] - first[m0[0]]+1

        for k,v in m[1:]:
            if v != m0[1]:
                break
            result = min(last[k] - first[k]+1,result)

        return result
