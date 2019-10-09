class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        return len(m.values()) == len(set(m.values()))
