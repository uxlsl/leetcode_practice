class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = set()
        for i in range(nums):
            if i not in ret:
                ret.add(i)
            else:
                ret.remove(i)
        return list(ret)
