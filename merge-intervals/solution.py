class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        result = [intervals[0]]
        j = 1
        while j < len(intervals):
            if result[-1][0] <= intervals[j][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[j][1])
            else:
                result.append(intervals[j])
            j += 1
        return result
