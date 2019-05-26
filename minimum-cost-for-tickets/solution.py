class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        total = 0
        m = {0:1,1:7,2:30}
        while days:
            best_choice = 0
            avg_price = costs[0]
            eat = {0:1}
            for choice in [1,2]:
                start = days[0]
                end = start + m[choice] - 1
                count = 0
                avg_price = costs[0]
                index = None
                for index,day in enumerate(days):
                    if day > end:
                        eat[choice] = index
                        break
                    count += 1
                else:
                    eat[choice] = index + 1
                if costs[choice] / count < avg_price:
                    best_choice = choice
                    avg_price = costs[choice] / count
            total += costs[best_choice]
            days = days[eat[best_choice]:]
        return total
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)
