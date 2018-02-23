class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = {}
        for i,v in enumerate(nums):
            print(record)
            if v in record and (i - record[v]) <= k:
                return True
            record[v] = i
        return False
