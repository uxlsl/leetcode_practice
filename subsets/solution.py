class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        ret = []
        for i in range(1,len(nums)):
            for j in itertools.combinations(nums,i):
                ret.append(j)

        ret.append([])
        ret.append(nums)


        return ret
