class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        record = {}
        for i,v in enumerate(cost):
            if i == 0:
                record[i] = v
            elif i == 1:
                record[i] = v
            else:
                record[i] = min(record[i-2] + v, record[i-1] + v)
        return min(record[i], record[i-1])

