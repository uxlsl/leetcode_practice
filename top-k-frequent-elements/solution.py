class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        nums = collections.Counter(nums)
        return [i[0] for i in nums.most_common(k)]
