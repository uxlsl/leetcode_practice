class Solution(object):
    def twoCitySchedCost(self, costs):
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
