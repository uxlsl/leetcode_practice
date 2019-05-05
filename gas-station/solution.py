class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        j = -1
        i = 0
        sum = 0
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                j = i
                sum = 0

        return j + 1 if total >= 0 else -1
