class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        return a.pop()
