class Solution:
    def findPairs1(self, nums, k):
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
            m[i - k] -= 1
            if m[i] >= 0 and m[i - k] >= 0:
                result.add((i - k, i))
            m[i] += 1
            m[i - k] += 1

            m[i] -= 1
            m[i + k] -= 1
            if m[i] >= 0 and m[i + k] >= 0:
                result.add((i, i + k))
            m[i] += 1
            m[i + k] += 1

        return len(result)

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        m = {}
        for i, v in enumerate(nums):
            m[v] = i
        count = 0
        for j, v in enumerate(nums):
            if v + k in m and m[v + k] != j:
                count += 1
                del m[v + k]  # 为什么
        return count
