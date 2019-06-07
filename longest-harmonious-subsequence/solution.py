from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        a = Counter(nums).most_common()
        a = sorted(a, key=lambda x:x[0])
        l = None
        for i in range(0, len(a)-1):
            if abs(a[i][0] - a[i+1][0])<=1:
                if l is None:
                    l = a[i][1] - a[i+1][1]
                else:
                    l = max(l, a[i][1] - a[i+1][1])

        return l


