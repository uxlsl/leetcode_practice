# leetcode
# https://leetcode-cn.com/problems/car-pooling/
# 上车下车怎么表示
import heapq


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        trips = sorted(trips, key=lambda x: x[1])
        cap = 0
        h = []
        for item in trips:
            # 下车
            while h:
                x = heapq.heappop(h)
                if x[1][2] > item[1]:
                    heapq.heappush(h,x)
                    break
                cap -= x[1][0]
            # 上车
            cap += item[0]
            if cap > capacity:
                return False
            heapq.heappush(h, (item[2], item))
        return True
