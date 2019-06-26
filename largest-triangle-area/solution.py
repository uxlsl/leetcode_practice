class Solution(object):
    def ares(self,p1,p2,p3):
        x1,y1 = p1
        x2,y2 = p2
        x3,y3 = p3
        return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        for x in points:
            for y in points:
                for z in points:
                    res = max(res, 0.5 * (x[0] * y[1] + y[0] * z[1] + z[0] * x[1]
                                          - x[0] * z[1] - y[0] * x[1] - z[0] * y[1]));
        return res
