
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict

        to = defaultdict(list)
        for i in times:
            to[i[0]].append(i)

        X = [(K, 0)]

        record = {K:0}
        while X:
            Y = []
            for x in X:
                for y in to[x[0]]:
                    cost = x[1] + y[2]
                    if y[1] in record and record[y[1]] <= cost:
                        continue
                    record[y[1]] = cost
                    Y.append((y[1], cost))
            X = Y

        if len(record) == N:
            return max(record.values())
        return -1
