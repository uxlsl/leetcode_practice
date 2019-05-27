class Solution(object):
    def twoCitySchedCost_worng(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key=lambda x: x[0])
        result = 0
        while costs:
            a = costs[0][0]
            b = costs[1][1]
            min_cost = costs[0][0] + costs[1][1]
            min_index = 1
            for index, item in enumerate(costs[1:], 1):
                if min_cost > a + item[1]:
                    min_cost = a + item[1]
                    min_index = index
            del costs[min_index]
            del costs[0]
            result += min_cost
        return result

    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key=lambda x: x[1] - x[0])
        total = 0
        for i in range(0, len(costs) // 2):
            j = len(costs) - i - 1
            total += costs[i][1] + costs[j][0]
        return total
