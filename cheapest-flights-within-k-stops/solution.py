class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        to = defaultdict(list)
        for i in flights:
            to[i[0]].append(i)

        X = [(src, 0)]
        record = {}  # 记录当前最少的值，便于剪掉不用的
        cost = -1
        for _ in range(K+1):  #  最多转机次数
            Y = []
            for x in X:
                for y in to[x[0]]:
                    if y[1] in record and x[1] + y[2] > record[y[1]]:
                        continue
                    record[y[1]] = x[1] + y[2]
                    if y[1] == dst:
                        if cost == -1:
                            cost = x[1] + y[2]
                        else:
                            cost = min(cost, x[1] + y[2])
                    else:
                        Y.append((y[1], x[1]+y[2]))
            X = Y
        return cost
