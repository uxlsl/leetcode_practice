class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        if len(wall) == 0:
            return 0

        m = defaultdict(int)
        for i in wall:
            total = 0
            for j in i[:-1]:
                total += j
                m[total] += 1

        if not m:
            return len(wall)
        item = max(m.items(), key=lambda x: x[1])
        return len(wall) - item[1]
