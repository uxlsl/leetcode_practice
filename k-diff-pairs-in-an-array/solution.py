class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        from collections import defaultdict
        m = defaultdict(int)
        for i in nums:
                m[i] += 1

        result = set()
        for i in nums:

            m[i] -= 1
            m[i-k] -= 1
            if m[i] >= 0 and m[i-k] >= 0:
                result.add((i-k, i))
            m[i] += 1
            m[i-k] += 1

            m[i] -= 1
            m[i+k] -= 1
            if m[i] >= 0 and m[i+k] >= 0:
                result.add((i, i+k))
            m[i] += 1
            m[i+k] += 1
 
        return len(result)

